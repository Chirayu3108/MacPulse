import psutil

class SystemMonitor:
# CPU USAGE
  def get_cpu_usage(self) -> dict:
    cpu_avg = psutil.cpu_percent(interval=1) # this blocks the execution for 1 seccond but we will have to change this in future
    cpu_cores = psutil.cpu_percent(percpu=True)
    return{
      "cpu_average_usage" : cpu_avg,
      "cpu_per_core_usage" : cpu_cores
    }

  
  
# Memory Usage (RAM)
  def get_memory_usage(self) -> dict:
    sys_mem = psutil.virtual_memory()
    sys_total_mem = sys_mem.total / (1024**3)
    sys_used_mem = sys_mem.used / (1024**3)
    sys_avail_mem = sys_mem.available / (1024**3)
    sys_mem_usage = sys_mem.percent
    return {
      "total_memory": sys_total_mem,
      "used_memory" : sys_used_mem,
      "available_memory" : sys_avail_mem,
      "memory_usage_percentage" : sys_mem_usage
    }

# Disk Usage

  def get_disk_usage(self) -> dict:
    total_disk = psutil.disk_usage('/')
    disk_total = total_disk.total / (1024**3)
    disk_used = total_disk.used / (1024**3)
    disk_free = total_disk.free / (1024**3)
    disk_usage_percentage = total_disk.percent
    return{
      "total_storage" : disk_total,
      "storage_used" : disk_used,
      "storage_free" : disk_free,
      "storage_usage_percentage" : disk_usage_percentage
    }

# Battery Status
  def get_battery_status(self) -> dict:
    battery = psutil.sensors_battery()
    if battery is not None: 
      bat_percent = battery.percent 
      bat_charge = battery.power_plugged 
      
      if battery.secsleft == psutil.POWER_TIME_UNLIMITED:
        charging_text = "The device is plugged in. Battery life is unlimited!"
      #elif battery.secsleft == psutil.POWER_TIME_UNKNOWN:
       # charging_text = "Calculating remaining time..."
      else:
        charging_text = battery.secsleft//60
    else:
      bat_percent = "Battery not found"
      bat_charge = "Battery not found"
      charging_text = "Battery not found"
      "No Battery dected in the system"

    bat_run_out = charging_text
    
    return{
      "battery_percentage" : bat_percent,
      "plugged_in" : bat_charge,
      "battery_run_out_in": bat_run_out
    }

# Testing all 

