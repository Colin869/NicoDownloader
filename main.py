import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import customtkinter as ctk
import threading
import os
import re
import requests
import json
import time
from urllib.parse import urlparse, parse_qs
import subprocess
import sys
from datetime import datetime

class NicoNicoDownloader:
    def __init__(self):
        # Set appearance mode
        ctk.set_appearance_mode("dark")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("NicoNico Video Downloader")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize variables
        self.download_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))
        self.url_var = tk.StringVar()
        self.quality_var = tk.StringVar(value="best")
        self.status_var = tk.StringVar(value="Ready to download")
        self.progress_var = tk.DoubleVar()
        
        # Download management
        self.download_queue = []
        self.current_download = None
        self.download_cancelled = False
        self.download_history = []
        
        # Load settings
        self.load_settings()
        
        # Create GUI elements
        self.create_widgets()
        
        # Check if yt-dlp is available
        self.check_ytdlp()
        
        # Load download history
        self.load_download_history()
    
    def create_widgets(self):
        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(main_frame, text="NicoNico Video Downloader", 
                                  font=ctk.CTkFont(size=24, weight="bold"))
        title_label.pack(pady=(20, 30))
        
        # URL input section
        url_frame = ctk.CTkFrame(main_frame)
        url_frame.pack(fill="x", padx=20, pady=10)
        
        url_label = ctk.CTkLabel(url_frame, text="Video URL:", font=ctk.CTkFont(size=14))
        url_label.pack(anchor="w", padx=20, pady=(20, 5))
        
        url_entry = ctk.CTkEntry(url_frame, textvariable=self.url_var, width=500, height=35,
                                placeholder_text="https://www.nicovideo.jp/watch/sm...")
        url_entry.pack(padx=20, pady=(0, 20))
        
        # Settings section
        settings_frame = ctk.CTkFrame(main_frame)
        settings_frame.pack(fill="x", padx=20, pady=10)
        
        settings_label = ctk.CTkLabel(settings_frame, text="Download Settings", 
                                    font=ctk.CTkFont(size=16, weight="bold"))
        settings_label.pack(anchor="w", padx=20, pady=(20, 15))
        
        # Quality selection
        quality_frame = ctk.CTkFrame(settings_frame)
        quality_frame.pack(fill="x", padx=20, pady=5)
        
        quality_label = ctk.CTkLabel(quality_frame, text="Quality:", font=ctk.CTkFont(size=12))
        quality_label.pack(side="left", padx=(20, 10))
        
        quality_combo = ctk.CTkComboBox(quality_frame, values=["best", "worst", "720p", "480p", "360p"],
                                       variable=self.quality_var, width=150, command=self.on_quality_change)
        quality_combo.pack(side="left", padx=(0, 20))
        
        # Download path selection
        path_frame = ctk.CTkFrame(settings_frame)
        path_frame.pack(fill="x", padx=20, pady=5)
        
        path_label = ctk.CTkLabel(path_frame, text="Save to:", font=ctk.CTkFont(size=12))
        path_label.pack(side="left", padx=(20, 10))
        
        path_entry = ctk.CTkEntry(path_frame, textvariable=self.download_path, width=350)
        path_entry.pack(side="left", padx=(0, 10))
        
        browse_btn = ctk.CTkButton(path_frame, text="Browse", width=80, command=self.browse_folder)
        browse_btn.pack(side="left")
        
        # Download buttons frame
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(pady=20)
        
        download_btn = ctk.CTkButton(button_frame, text="Download Video", 
                                   command=self.start_download, height=40, width=150,
                                   font=ctk.CTkFont(size=16, weight="bold"))
        download_btn.pack(side="left", padx=(0, 10))
        
        self.cancel_btn = ctk.CTkButton(button_frame, text="Cancel Download", 
                                      command=self.cancel_download, height=40, width=150,
                                      font=ctk.CTkFont(size=14), state="disabled")
        self.cancel_btn.pack(side="left")
        
        # Progress section
        progress_frame = ctk.CTkFrame(main_frame)
        progress_frame.pack(fill="x", padx=20, pady=10)
        
        progress_label = ctk.CTkLabel(progress_frame, text="Progress", 
                                    font=ctk.CTkFont(size=14, weight="bold"))
        progress_label.pack(anchor="w", padx=20, pady=(20, 10))
        
        self.progress_bar = ctk.CTkProgressBar(progress_frame)
        self.progress_bar.pack(fill="x", padx=20, pady=(0, 10))
        self.progress_bar.set(0)
        
        # Status label
        status_label = ctk.CTkLabel(progress_frame, textvariable=self.status_var, 
                                  font=ctk.CTkFont(size=12))
        status_label.pack(padx=20, pady=(0, 20))
        
        # Log section
        log_frame = ctk.CTkFrame(main_frame)
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Log header with utility buttons
        log_header_frame = ctk.CTkFrame(log_frame)
        log_header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        log_label = ctk.CTkLabel(log_header_frame, text="Download Log", 
                                font=ctk.CTkFont(size=14, weight="bold"))
        log_label.pack(side="left")
        
        clear_log_btn = ctk.CTkButton(log_header_frame, text="Clear Log", 
                                    command=self.clear_log, width=80, height=25)
        clear_log_btn.pack(side="right", padx=(10, 0))
        
        history_btn = ctk.CTkButton(log_header_frame, text="Show History", 
                                  command=self.show_download_history, width=100, height=25)
        history_btn.pack(side="right")
        
        # Create text widget with scrollbar
        text_frame = ctk.CTkFrame(log_frame)
        text_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        self.log_text = ctk.CTkTextbox(text_frame, height=150)
        self.log_text.pack(side="left", fill="both", expand=True)
        
        scrollbar = ctk.CTkScrollbar(text_frame, command=self.log_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_text.configure(yscrollcommand=scrollbar.set)
    
    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self.download_path.get())
        if folder:
            self.download_path.set(folder)
            self.save_settings()
    
    def load_settings(self):
        """Load application settings from file"""
        try:
            if os.path.exists("settings.json"):
                with open("settings.json", "r", encoding="utf-8") as f:
                    settings = json.load(f)
                    if "download_path" in settings:
                        self.download_path.set(settings["download_path"])
                    if "quality" in settings:
                        self.quality_var.set(settings["quality"])
        except Exception as e:
            self.log_message(f"Error loading settings: {str(e)}")
    
    def save_settings(self):
        """Save application settings to file"""
        try:
            settings = {
                "download_path": self.download_path.get(),
                "quality": self.quality_var.get(),
                "last_updated": datetime.now().isoformat()
            }
            with open("settings.json", "w", encoding="utf-8") as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.log_message(f"Error saving settings: {str(e)}")
    
    def load_download_history(self):
        """Load download history from file"""
        try:
            if os.path.exists("download_history.json"):
                with open("download_history.json", "r", encoding="utf-8") as f:
                    self.download_history = json.load(f)
        except Exception as e:
            self.log_message(f"Error loading download history: {str(e)}")
    
    def save_download_history(self):
        """Save download history to file"""
        try:
            with open("download_history.json", "w", encoding="utf-8") as f:
                json.dump(self.download_history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.log_message(f"Error saving download history: {str(e)}")
    
    def add_to_history(self, video_id, title, status, download_path):
        """Add download to history"""
        history_entry = {
            "video_id": video_id,
            "title": title,
            "status": status,
            "download_path": download_path,
            "timestamp": datetime.now().isoformat()
        }
        self.download_history.append(history_entry)
        # Keep only last 100 entries
        if len(self.download_history) > 100:
            self.download_history = self.download_history[-100:]
        self.save_download_history()
    
    def check_ytdlp(self):
        """Check if yt-dlp is available (non-blocking)"""
        try:
            # Try to import yt_dlp first (faster and safer)
            import yt_dlp
            self.log_message(f"yt-dlp version: {yt_dlp.version.__version__}")
        except ImportError:
            self.log_message("Warning: yt-dlp not properly installed")
        except Exception as e:
            self.log_message(f"Error checking yt-dlp: {str(e)}")
    
    def log_message(self, message):
        self.log_text.insert("end", f"{message}\n")
        self.log_text.see("end")
        self.root.update_idletasks()
    
    def validate_url(self, url):
        """Validate if the URL is a valid NicoNico video URL"""
        if not url:
            return False, "Please enter a URL"
        
        # Check if it's a NicoNico URL
        if "nicovideo.jp" not in url and "nico.ms" not in url:
            return False, "Please enter a valid NicoNico video URL"
        
        # Extract video ID
        video_id = self.extract_video_id(url)
        if not video_id:
            return False, "Could not extract video ID from URL"
        
        return True, video_id
    
    def extract_video_id(self, url):
        """Extract video ID from NicoNico URL"""
        # Handle different URL formats
        if "nico.ms" in url:
            # Short URL format
            try:
                response = requests.head(url, allow_redirects=True, timeout=10)
                url = response.url
            except requests.RequestException as e:
                self.log_message(f"Error resolving short URL: {str(e)}")
                return None
        
        # Extract from full URL
        patterns = [
            r"nicovideo\.jp/watch/([a-z]{2}\d+)",
            r"nicovideo\.jp/watch/(\d+)",
            r"watch/([a-z]{2}\d+)",
            r"watch/(\d+)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def get_video_info(self, url):
        """Get video information using yt-dlp"""
        try:
            # Use a more robust approach with shorter timeout
            cmd = [
                sys.executable, "-m", "yt_dlp",
                "--dump-json",
                "--no-playlist",
                "--no-warnings",
                url
            ]
            
            # Use a shorter timeout to prevent hanging
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            if result.returncode == 0:
                try:
                    video_info = json.loads(result.stdout)
                    return {
                        "title": video_info.get("title", "Unknown Title"),
                        "duration": video_info.get("duration", 0),
                        "uploader": video_info.get("uploader", "Unknown"),
                        "view_count": video_info.get("view_count", 0),
                        "upload_date": video_info.get("upload_date", ""),
                        "formats": video_info.get("formats", [])
                    }
                except json.JSONDecodeError:
                    self.log_message("Error parsing video info response")
                    return None
            else:
                self.log_message(f"Error getting video info: {result.stderr}")
                return None
        except subprocess.TimeoutExpired:
            self.log_message("Timeout getting video info - proceeding without preview")
            return None
        except Exception as e:
            self.log_message(f"Error getting video info: {str(e)}")
            return None
    
    def start_download(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a video URL")
            return
        
        # Get video info first (optional)
        self.status_var.set("Getting video information...")
        self.progress_bar.set(0.1)
        
        video_info = self.get_video_info(url)
        if video_info:
            self.log_message(f"Video: {video_info['title']} by {video_info['uploader']}")
        else:
            self.log_message("Proceeding without video preview...")
            # Create a minimal video_info structure so the app can continue
            video_info = {
                "title": "Unknown Title",
                "uploader": "Unknown"
            }
        
        # Validate URL
        is_valid, result = self.validate_url(url)
        if not is_valid:
            messagebox.showerror("Invalid URL", result)
            self.status_var.set("Ready to download")
            self.progress_bar.set(0)
            return
        
        video_id = result
        download_path = self.download_path.get()
        
        # Create download directory if it doesn't exist
        if not os.path.exists(download_path):
            try:
                os.makedirs(download_path)
            except Exception as e:
                messagebox.showerror("Error", f"Could not create download directory: {str(e)}")
                self.status_var.set("Ready to download")
                self.progress_bar.set(0)
                return
        
        # Add to download queue
        download_item = {
            "url": url,
            "video_id": video_id,
            "download_path": download_path,
            "video_info": video_info,
            "status": "queued"
        }
        
        self.download_queue.append(download_item)
        title = video_info.get('title', 'Unknown Title') if video_info else 'Unknown Title'
        self.log_message(f"Added to queue: {title}")
        
        # Start download if no other download is running
        if not self.current_download:
            self.process_download_queue()
    
    def process_download_queue(self):
        """Process the download queue"""
        if not self.download_queue or self.current_download:
            return
        
        download_item = self.download_queue.pop(0)
        self.current_download = download_item
        
        # Start download in separate thread
        self.status_var.set("Starting download...")
        self.progress_bar.set(0)
        self.update_button_states(downloading=True)
        
        download_thread = threading.Thread(target=self.download_video, 
                                        args=(download_item,))
        download_thread.daemon = True
        download_thread.start()
    
    def cancel_download(self):
        """Cancel current download"""
        if self.current_download:
            self.download_cancelled = True
            self.status_var.set("Cancelling download...")
            self.log_message("Download cancelled by user")
    
    def retry_download(self, download_item):
        """Retry a failed download"""
        download_item["status"] = "queued"
        download_item["retry_count"] = download_item.get("retry_count", 0) + 1
        
        if download_item["retry_count"] <= 3:
            self.download_queue.insert(0, download_item)
            title = download_item.get('video_info', {}).get('title', 'Unknown Title')
            self.log_message(f"Retrying download: {title}")
            if not self.current_download:
                self.process_download_queue()
        else:
            title = download_item.get('video_info', {}).get('title', 'Unknown Title')
            self.log_message(f"Max retries reached for: {title}")
            self.add_to_history(
                download_item["video_id"],
                title,
                "failed",
                download_item["download_path"]
            )
    
    def download_video(self, download_item):
        """Download video with improved progress tracking and error handling"""
        try:
            url = download_item["url"]
            video_id = download_item["video_id"]
            download_path = download_item["download_path"]
            video_info = download_item["video_info"]
            
            self.status_var.set("Downloading video...")
            title = video_info.get('title', 'Unknown Title') if video_info else 'Unknown Title'
            self.log_message(f"Starting download for: {title}")
            self.log_message(f"Video ID: {video_id}")
            self.log_message(f"Download path: {download_path}")
            
            # Reset cancellation flag
            self.download_cancelled = False
            
            # Build yt-dlp command with better options
            cmd = [
                sys.executable, "-m", "yt_dlp",
                "--format", f"best[height<={self.quality_var.get()}]" if self.quality_var.get() in ["720p", "480p", "360p"] else self.quality_var.get(),
                "--output", os.path.join(download_path, f"%(title)s.%(ext)s"),
                "--write-description",
                "--write-thumbnail",
                "--add-metadata",
                "--newline",
                "--progress",
                url
            ]
            
            self.log_message(f"Running command: {' '.join(cmd)}")
            
            # Run yt-dlp with real-time output
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                     universal_newlines=True, bufsize=1)
            
            # Monitor progress with better parsing
            start_time = time.time()
            for line in process.stdout:
                if self.download_cancelled:
                    process.terminate()
                    self.log_message("Download cancelled by user")
                    break
                
                if line:
                    line = line.strip()
                    self.log_message(line)
                    
                    # Update progress based on various patterns
                    self.update_progress_from_line(line, start_time)
            
            # Wait for process to complete
            process.wait()
            
            if self.download_cancelled:
                self.status_var.set("Download cancelled")
                self.add_to_history(video_id, title, "cancelled", download_path)
            elif process.returncode == 0:
                self.status_var.set("Download completed successfully!")
                self.progress_bar.set(1.0)
                self.log_message("Download completed successfully!")
                self.add_to_history(video_id, title, "completed", download_path)
                messagebox.showinfo("Success", f"Video '{title}' downloaded successfully!")
            else:
                self.status_var.set("Download failed")
                self.log_message("Download failed!")
                self.add_to_history(video_id, title, "failed", download_path)
                
                # Offer retry option
                if messagebox.askyesno("Download Failed", 
                                     f"Download failed for '{title}'. Would you like to retry?"):
                    self.retry_download(download_item)
                else:
                    messagebox.showerror("Error", "Download failed. Check the log for details.")
                
        except Exception as e:
            self.status_var.set("Download error")
            self.log_message(f"Error during download: {str(e)}")
            self.add_to_history(video_id, title, "error", download_path)
            messagebox.showerror("Error", f"Download error: {str(e)}")
        
        finally:
            self.progress_bar.set(0)
            self.current_download = None
            self.download_cancelled = False
            self.update_button_states(downloading=False)
            
            # Process next item in queue
            if self.download_queue:
                self.process_download_queue()
            else:
                self.status_var.set("Ready to download")
    
    def update_progress_from_line(self, line, start_time):
        """Update progress bar based on yt-dlp output"""
        try:
            # Look for percentage patterns
            percent_patterns = [
                r"(\d+\.?\d*)%",
                r"Downloading.*?(\d+\.?\d*)%",
                r"(\d+\.?\d*)% of ~"
            ]
            
            for pattern in percent_patterns:
                match = re.search(pattern, line)
                if match:
                    percent = float(match.group(1)) / 100
                    self.progress_bar.set(percent)
                    break
            
            # Look for download speed
            speed_match = re.search(r"(\d+\.?\d*\s*[KMGT]iB/s)", line)
            if speed_match:
                speed = speed_match.group(1)
                elapsed = time.time() - start_time
                self.status_var.set(f"Downloading... {speed} - {elapsed:.1f}s")
            
            # Look for ETA
            eta_match = re.search(r"ETA (\d+:\d+)", line)
            if eta_match:
                eta = eta_match.group(1)
                self.status_var.set(f"Downloading... ETA: {eta}")
                
        except Exception as e:
            # Ignore progress parsing errors
            pass
    
    def on_quality_change(self, choice):
        """Handle quality selection change"""
        self.save_settings()
        self.log_message(f"Quality changed to: {choice}")
    
    def update_button_states(self, downloading=False):
        """Update button states based on download status"""
        if downloading:
            self.cancel_btn.configure(state="normal")
        else:
            self.cancel_btn.configure(state="disabled")
    
    def clear_log(self):
        """Clear the download log"""
        self.log_text.delete("1.0", "end")
        self.log_message("Log cleared")
    
    def show_download_history(self):
        """Show download history in a new window"""
        if not self.download_history:
            messagebox.showinfo("Download History", "No download history available.")
            return
        
        history_window = ctk.CTkToplevel(self.root)
        history_window.title("Download History")
        history_window.geometry("600x400")
        
        # Create history display
        history_frame = ctk.CTkFrame(history_window)
        history_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        history_label = ctk.CTkLabel(history_frame, text="Download History", 
                                   font=ctk.CTkFont(size=18, weight="bold"))
        history_label.pack(pady=(0, 20))
        
        # Create scrollable history list
        history_text = ctk.CTkTextbox(history_frame, height=300)
        history_text.insert("end", "Download History\n")
        history_text.pack(fill="both", expand=True)
        
        for entry in reversed(self.download_history[-50:]):  # Show last 50 entries
            timestamp = datetime.fromisoformat(entry["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
            status_icon = "✅" if entry["status"] == "completed" else "❌" if entry["status"] == "failed" else "⏸️"
            history_text.insert("end", f"{status_icon} {timestamp} - {entry['title']} ({entry['status']})\n")
        
        history_text.configure(state="disabled")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NicoNicoDownloader()
    app.run()
