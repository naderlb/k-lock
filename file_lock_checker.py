import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys
import ctypes
from ctypes import wintypes
import psutil
import threading
import time
from datetime import datetime

class KLock:
    def __init__(self, root):
        self.root = root
        self.root.title("K-Lock Professional - File & Folder Lock Manager")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Set application icon and styling
        self.root.configure(bg='#f0f0f0')
        
        # Configure ttk styles for professional look
        self.setup_styles()
        
        # Windows API constants
        self.GENERIC_READ = 0x80000000
        self.GENERIC_WRITE = 0x40000000
        self.OPEN_EXISTING = 3
        self.FILE_SHARE_READ = 0x00000001
        self.FILE_SHARE_WRITE = 0x00000002
        self.FILE_SHARE_DELETE = 0x00000004
        
        self.setup_ui()
        self.setup_windows_api()
    
    def setup_styles(self):
        """Configure professional styling for the application"""
        style = ttk.Style()
        
        # Configure custom styles
        style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'), foreground='#2c3e50')
        style.configure('Header.TLabel', font=('Segoe UI', 12, 'bold'), foreground='#34495e')
        style.configure('Status.TLabel', font=('Segoe UI', 11, 'bold'))
        style.configure('Info.TLabel', font=('Segoe UI', 10))
        style.configure('Action.TButton', font=('Segoe UI', 10, 'bold'))
        style.configure('Danger.TButton', font=('Segoe UI', 10, 'bold'))
        
        # Configure frame styles
        style.configure('Card.TFrame', relief='solid', borderwidth=1)
        style.configure('Header.TFrame', background='#3498db', relief='flat')
    
    def setup_windows_api(self):
        """Setup Windows API functions"""
        self.kernel32 = ctypes.windll.kernel32
        self.ntdll = ctypes.windll.ntdll
        
        # Define function signatures
        self.kernel32.CreateFileW.argtypes = [
            wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
            wintypes.LPVOID, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE
        ]
        self.kernel32.CreateFileW.restype = wintypes.HANDLE
        
        self.kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
        self.kernel32.CloseHandle.restype = wintypes.BOOL
        
        # Define Windows API structure inside the class
        class BY_HANDLE_FILE_INFORMATION(ctypes.Structure):
            _fields_ = [
                ("dwFileAttributes", wintypes.DWORD),
                ("ftCreationTime", wintypes.FILETIME),
                ("ftLastAccessTime", wintypes.FILETIME),
                ("ftLastWriteTime", wintypes.FILETIME),
                ("dwVolumeSerialNumber", wintypes.DWORD),
                ("nFileSizeHigh", wintypes.DWORD),
                ("nFileSizeLow", wintypes.DWORD),
                ("nNumberOfLinks", wintypes.DWORD),
                ("nFileIndexHigh", wintypes.DWORD),
                ("nFileIndexLow", wintypes.DWORD),
            ]
        
        self.BY_HANDLE_FILE_INFORMATION = BY_HANDLE_FILE_INFORMATION
        
        self.kernel32.GetFileInformationByHandle.argtypes = [
            wintypes.HANDLE, ctypes.POINTER(self.BY_HANDLE_FILE_INFORMATION)
        ]
        self.kernel32.GetFileInformationByHandle.restype = wintypes.BOOL
    
    def setup_ui(self):
        """Setup the user interface"""
        # Header frame
        header_frame = ttk.Frame(self.root, style='Header.TFrame', padding="15")
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=0, pady=0)
        
        # Title and subtitle
        title_label = ttk.Label(header_frame, text="K-Lock Professional", style='Title.TLabel', background='#3498db', foreground='white')
        title_label.pack(side=tk.LEFT)
        
        subtitle_label = ttk.Label(header_frame, text="Advanced File & Folder Lock Manager", style='Info.TLabel', background='#3498db', foreground='#ecf0f1')
        subtitle_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # File/Folder selection card
        selection_card = ttk.LabelFrame(main_frame, text="Target Selection", style='Card.TFrame', padding="15")
        selection_card.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        selection_card.columnconfigure(1, weight=1)
        
        ttk.Label(selection_card, text="File or Folder Path:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        self.file_path_var = tk.StringVar()
        file_entry = ttk.Entry(selection_card, textvariable=self.file_path_var, width=60, font=('Consolas', 10))
        file_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Browse buttons frame
        browse_frame = ttk.Frame(selection_card)
        browse_frame.grid(row=2, column=0, columnspan=2, sticky=tk.W)
        
        browse_file_btn = ttk.Button(browse_frame, text="📁 Browse File", command=self.browse_file, style='Action.TButton')
        browse_file_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        browse_folder_btn = ttk.Button(browse_frame, text="📂 Browse Folder", command=self.browse_folder, style='Action.TButton')
        browse_folder_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        check_btn = ttk.Button(browse_frame, text="🔍 Analyze Lock Status", command=self.check_file_lock, style='Action.TButton')
        check_btn.pack(side=tk.LEFT)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Lock Analysis Results", style='Card.TFrame', padding="15")
        results_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(2, weight=1)
        
        # Status header
        status_header_frame = ttk.Frame(results_frame)
        status_header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.lock_status_var = tk.StringVar(value="🔍 Ready to analyze file/folder lock status")
        status_label = ttk.Label(status_header_frame, textvariable=self.lock_status_var, style='Status.TLabel')
        status_label.pack(side=tk.LEFT)
        
        # Timestamp
        self.timestamp_var = tk.StringVar()
        timestamp_label = ttk.Label(status_header_frame, textvariable=self.timestamp_var, style='Info.TLabel')
        timestamp_label.pack(side=tk.RIGHT)
        
        # Results text area with better styling
        text_frame = ttk.Frame(results_frame)
        text_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        self.results_text = tk.Text(text_frame, height=12, width=80, wrap=tk.WORD, 
                                  font=('Consolas', 9), bg='#f8f9fa', fg='#2c3e50',
                                  relief='flat', borderwidth=1)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Action buttons frame
        action_frame = ttk.Frame(results_frame)
        action_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        self.release_btn = ttk.Button(action_frame, text="⚠️ Force Release Lock", command=self.release_lock, 
                                    state=tk.DISABLED, style='Danger.TButton')
        self.release_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        refresh_btn = ttk.Button(action_frame, text="🔄 Refresh Analysis", command=self.check_file_lock, style='Action.TButton')
        refresh_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = ttk.Button(action_frame, text="🗑️ Clear Results", command=self.clear_results, style='Action.TButton')
        clear_btn.pack(side=tk.LEFT)
        
        # Configure main frame grid weights
        main_frame.rowconfigure(1, weight=1)
    
    def browse_file(self):
        """Open file dialog to select a file"""
        file_path = filedialog.askopenfilename(
            title="K-Lock: Select File to Analyze",
            filetypes=[("All Files", "*.*"), ("Documents", "*.doc;*.docx;*.pdf;*.txt"), 
                      ("Images", "*.jpg;*.jpeg;*.png;*.gif;*.bmp"), ("Videos", "*.mp4;*.avi;*.mkv;*.mov")]
        )
        if file_path:
            self.file_path_var.set(file_path)
            self.check_file_lock()
    
    def browse_folder(self):
        """Open folder dialog to select a folder"""
        folder_path = filedialog.askdirectory(
            title="K-Lock: Select Folder to Analyze"
        )
        if folder_path:
            self.file_path_var.set(folder_path)
            self.check_file_lock()
    
    def clear_results(self):
        """Clear the results text area"""
        self.results_text.delete(1.0, tk.END)
        self.lock_status_var.set("🔍 Ready to analyze file/folder lock status")
        self.timestamp_var.set("")
        self.release_btn.config(state=tk.DISABLED)
    
    def check_file_lock(self):
        """Check if the selected file or folder is locked"""
        file_path = self.file_path_var.get()
        if not file_path or not os.path.exists(file_path):
            messagebox.showerror("K-Lock Error", "Please select a valid file or folder to analyze.")
            return
        
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        self.lock_status_var.set("🔍 Analyzing lock status...")
        self.timestamp_var.set(f"Started: {datetime.now().strftime('%H:%M:%S')}")
        self.release_btn.config(state=tk.DISABLED)
        
        # Run check in separate thread to avoid UI freezing
        thread = threading.Thread(target=self._check_file_lock_thread, args=(file_path,))
        thread.daemon = True
        thread.start()
    
    def _check_file_lock_thread(self, file_path):
        """Thread function to check file lock"""
        try:
            # Convert to absolute path
            abs_path = os.path.abspath(file_path)
            
            # Check if file is locked
            is_locked, lock_info = self.is_file_locked(abs_path)
            
            # Update UI in main thread
            self.root.after(0, self._update_results, is_locked, lock_info, abs_path)
            
        except Exception as e:
            self.root.after(0, self._show_error, f"Error checking file lock: {str(e)}")
    
    def _update_results(self, is_locked, lock_info, file_path):
        """Update the results in the UI"""
        self.timestamp_var.set(f"Completed: {datetime.now().strftime('%H:%M:%S')}")
        
        if is_locked:
            self.lock_status_var.set("🔒 LOCKED - File/Folder is in use")
            self.release_btn.config(state=tk.NORMAL)
            
            # Display detailed lock information with professional formatting
            self.results_text.insert(tk.END, "=" * 80 + "\n")
            self.results_text.insert(tk.END, "K-LOCK ANALYSIS REPORT\n")
            self.results_text.insert(tk.END, "=" * 80 + "\n\n")
            
            self.results_text.insert(tk.END, f"Target: {file_path}\n")
            self.results_text.insert(tk.END, f"Type: {'Folder' if os.path.isdir(file_path) else 'File'}\n")
            self.results_text.insert(tk.END, f"Status: LOCKED ❌\n")
            self.results_text.insert(tk.END, f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            if lock_info:
                self.results_text.insert(tk.END, "LOCKING PROCESSES DETECTED:\n")
                self.results_text.insert(tk.END, "-" * 80 + "\n\n")
                
                for i, process in enumerate(lock_info, 1):
                    self.results_text.insert(tk.END, f"[{i}] Process Information:\n")
                    self.results_text.insert(tk.END, f"    PID: {process['pid']}\n")
                    self.results_text.insert(tk.END, f"    Name: {process['name']}\n")
                    self.results_text.insert(tk.END, f"    Executable: {process['exe']}\n")
                    self.results_text.insert(tk.END, f"    Command: {process['cmdline']}\n")
                    self.results_text.insert(tk.END, "-" * 40 + "\n\n")
            else:
                self.results_text.insert(tk.END, "No specific process information available.\n")
                self.results_text.insert(tk.END, "The file/folder may be locked by system processes.\n\n")
        else:
            self.lock_status_var.set("✅ UNLOCKED - File/Folder is accessible")
            self.release_btn.config(state=tk.DISABLED)
            
            self.results_text.insert(tk.END, "=" * 80 + "\n")
            self.results_text.insert(tk.END, "K-LOCK ANALYSIS REPORT\n")
            self.results_text.insert(tk.END, "=" * 80 + "\n\n")
            
            self.results_text.insert(tk.END, f"Target: {file_path}\n")
            self.results_text.insert(tk.END, f"Type: {'Folder' if os.path.isdir(file_path) else 'File'}\n")
            self.results_text.insert(tk.END, f"Status: UNLOCKED ✅\n")
            self.results_text.insert(tk.END, f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            self.results_text.insert(tk.END, "The file/folder is accessible and not locked by any process.\n")
            self.results_text.insert(tk.END, "You can safely perform operations on this target.\n\n")
    
    def _show_error(self, error_msg):
        """Show error message"""
        self.lock_status_var.set("❌ Analysis Failed")
        self.timestamp_var.set(f"Error: {datetime.now().strftime('%H:%M:%S')}")
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "=" * 80 + "\n")
        self.results_text.insert(tk.END, "K-LOCK ERROR REPORT\n")
        self.results_text.insert(tk.END, "=" * 80 + "\n\n")
        self.results_text.insert(tk.END, f"Error: {error_msg}\n")
        self.results_text.insert(tk.END, f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        self.results_text.insert(tk.END, "Please check the file/folder path and try again.\n")
        messagebox.showerror("K-Lock Error", error_msg)
    
    def is_file_locked(self, file_path):
        """Check if a file is locked and return process information"""
        try:
            # Try to open the file with exclusive access
            handle = self.kernel32.CreateFileW(
                file_path,
                self.GENERIC_READ | self.GENERIC_WRITE,
                0,  # No sharing
                None,
                self.OPEN_EXISTING,
                0,
                None
            )
            
            if handle == wintypes.HANDLE(-1).value:  # INVALID_HANDLE_VALUE
                # File is locked, find which processes are using it
                locking_processes = self.find_processes_using_file(file_path)
                return True, locking_processes
            else:
                # File is not locked
                self.kernel32.CloseHandle(handle)
                return False, None
                
        except Exception as e:
            raise Exception(f"Failed to check file lock: {str(e)}")
    
    def find_processes_using_file(self, file_path):
        """Find processes that are using the specified file or folder"""
        processes = []
        abs_path = os.path.abspath(file_path)
        
        try:
            # Method 1: Check open files
            for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline', 'open_files']):
                try:
                    # Check if process has files open
                    if hasattr(proc.info, 'open_files') and proc.info['open_files']:
                        for open_file in proc.info['open_files']:
                            open_path = os.path.abspath(open_file.path)
                            
                            # Check for exact match
                            if open_path == abs_path:
                                processes.append({
                                    'pid': proc.info['pid'],
                                    'name': proc.info['name'],
                                    'exe': proc.info['exe'] or 'Unknown',
                                    'cmdline': ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else 'Unknown'
                                })
                                break
                            
                            # Check if it's a folder and the open file is inside it
                            elif os.path.isdir(abs_path) and open_path.startswith(abs_path + os.sep):
                                processes.append({
                                    'pid': proc.info['pid'],
                                    'name': proc.info['name'],
                                    'exe': proc.info['exe'] or 'Unknown',
                                    'cmdline': ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else 'Unknown'
                                })
                                break
                    
                    # Method 2: Check working directory
                    try:
                        proc_obj = psutil.Process(proc.info['pid'])
                        cwd = proc_obj.cwd()
                        if cwd and (cwd == abs_path or (os.path.isdir(abs_path) and cwd.startswith(abs_path + os.sep))):
                            processes.append({
                                'pid': proc.info['pid'],
                                'name': proc.info['name'],
                                'exe': proc.info['exe'] or 'Unknown',
                                'cmdline': ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else 'Unknown'
                            })
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
            
            # Method 3: Use Windows handle command if available
            processes.extend(self._find_processes_with_handle(abs_path))
                    
        except Exception as e:
            print(f"Error finding processes: {e}")
        
        # Remove duplicates based on PID
        seen_pids = set()
        unique_processes = []
        for proc in processes:
            if proc['pid'] not in seen_pids:
                unique_processes.append(proc)
                seen_pids.add(proc['pid'])
        
        return unique_processes
    
    def _find_processes_with_handle(self, file_path):
        """Use Windows handle.exe to find processes using the file/folder"""
        processes = []
        
        try:
            # Try to use handle.exe if available
            import subprocess
            result = subprocess.run(['handle.exe', file_path], 
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'pid:' in line.lower() and ':' in line:
                        try:
                            # Parse handle.exe output
                            parts = line.split()
                            pid = None
                            name = 'Unknown'
                            
                            for i, part in enumerate(parts):
                                if part.lower().startswith('pid:'):
                                    pid = int(part.split(':')[1])
                                elif pid and i > 0:
                                    name = part
                                    break
                            
                            if pid:
                                processes.append({
                                    'pid': pid,
                                    'name': name,
                                    'exe': 'Unknown',
                                    'cmdline': 'Found via handle.exe'
                                })
                        except (ValueError, IndexError):
                            continue
        except (FileNotFoundError, subprocess.TimeoutExpired, subprocess.CalledProcessError):
            # handle.exe not available or failed
            pass
        except Exception as e:
            print(f"Error using handle.exe: {e}")
        
        return processes
    
    def release_lock(self):
        """Release file lock by terminating processes"""
        file_path = self.file_path_var.get()
        if not file_path:
            return
        
        # Get current lock information
        is_locked, lock_info = self.is_file_locked(file_path)
        
        if not is_locked or not lock_info:
            messagebox.showinfo("K-Lock Info", "File/folder is not locked or no locking processes found.")
            return
        
        # Ask for confirmation with professional dialog
        process_list = "\n".join([f"• {p['name']} (PID: {p['pid']})" for p in lock_info])
        result = messagebox.askyesno(
            "K-Lock: Confirm Force Release",
            f"⚠️ WARNING: Force Release Operation\n\n"
            f"The following processes are locking the target:\n\n{process_list}\n\n"
            f"Terminating these processes will:\n"
            f"• Close the applications immediately\n"
            f"• Release the file/folder lock\n"
            f"• May cause data loss if unsaved work exists\n\n"
            f"Are you sure you want to proceed?"
        )
        
        if result:
            self._release_lock_thread(lock_info)
    
    def _release_lock_thread(self, lock_info):
        """Thread function to release file lock"""
        try:
            terminated_count = 0
            
            for process_info in lock_info:
                try:
                    proc = psutil.Process(process_info['pid'])
                    proc.terminate()
                    
                    # Wait for process to terminate
                    try:
                        proc.wait(timeout=5)
                        terminated_count += 1
                    except psutil.TimeoutExpired:
                        # Force kill if it doesn't terminate gracefully
                        proc.kill()
                        terminated_count += 1
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            # Update UI
            self.root.after(0, self._lock_release_complete, terminated_count)
            
        except Exception as e:
            self.root.after(0, self._show_error, f"Error releasing lock: {str(e)}")
    
    def _lock_release_complete(self, terminated_count):
        """Handle lock release completion"""
        if terminated_count > 0:
            messagebox.showinfo("K-Lock Success", 
                              f"✅ Successfully terminated {terminated_count} process(es).\n\n"
                              f"The file/folder lock has been released.\n"
                              f"Refreshing analysis...")
            # Refresh the lock status
            self.check_file_lock()
        else:
            messagebox.showwarning("K-Lock Warning", 
                                 "⚠️ No processes were terminated.\n\n"
                                 "The file/folder may still be locked by:\n"
                                 "• System processes\n"
                                 "• Processes with higher privileges\n"
                                 "• Processes that couldn't be accessed")

# Windows API structures are now defined inside the KLock class

def main():
    """Main function to run the K-Lock application"""
    try:
        root = tk.Tk()
        app = KLock(root)
        
        # Center the window on screen
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        
        root.mainloop()
    except Exception as e:
        messagebox.showerror("K-Lock Fatal Error", f"Failed to start K-Lock application: {str(e)}")

if __name__ == "__main__":
    main()
