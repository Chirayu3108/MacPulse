import psutil

class SystemMonitor:
# CPU USAGE
  def get_cpu_usage(self) -> None:
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
    disk_usage = psutil.disk_usage('/')
    print(f"{disk_usage.total / (1024**3):.2f}GB")
  

comp = SystemMonitor()
comp.get_disk_usage()


