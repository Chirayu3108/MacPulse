import psutil

class SystemMonitor:
# CPU USAGE
  def get_cpu_usage(self):
    cpu_avg = psutil.cpu_percent(interval=1)
    cpu_cores = psutil.cpu_percent(percpu=True)
   


  
# Memory Usage (RAM)
  def get_memory_usage(self):
    sys_mem = psutil.virtual_memory()
    sys_total_mem = f"{sys_mem.total / (1024**3)}GB"
    sys_used_mem = f"{sys_mem.used / (1024**3):.2f}GB"
    sys_avail_mem = f"{sys_mem.available / (1024**3):.2f}GB"
    sys_mem_usage = (f"{sys_mem.percent}%")

# Disk Usage

  def get_disk_usage(self):
    total_disk = psutil.disk_usage('/')
    disk_total = f"{total_disk.total / (1024**3):.2f}GB"
    disk_used = f"{total_disk.used / (1024**3):.2f}GB"
    disk_free = f"{total_disk.free / (1024**3):.2f}GB"
    disk_usage_percentage = f"{total_disk.percent}%"

# Battery Status
  def get_battery_status(self):
    battery = psutil.sensors_battery()
    bat_percent = f"{battery.percent}%" if battery is not None else "N/A"
    bat_charge = f"{battery.power_plugged}" if battery is not None else "N/A"
    bat_run_out = f"{battery.secsleft / 60} mins" if battery is not None else "N/A"

    


