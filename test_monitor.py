from monitor import SystemMonitor

Mac = SystemMonitor()
print(Mac.get_cpu_usage())
print(Mac.get_memory_usage())
print(Mac.get_battery_status())
print(Mac.get_disk_usage())