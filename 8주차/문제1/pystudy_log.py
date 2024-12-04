from server_log import log_manager

# read_logs
log_manager.read_logs('./server_log/logs.txt')
print('\n')

# filter_logs
logs = log_manager.li
filtered_logs = log_manager.filter_logs(logs, "ERROR")
print(filtered_logs)
print('\n')

# save_logs
log_manager.save_logs(filtered_logs, 'error_logs.txt')