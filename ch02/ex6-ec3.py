# The server is configured as:
# LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined
# %h - client_ip
# %l - identd of the client (almost always off)
# %u - user id from HTTP auth (almost always not used)
# %t - timestamp in DD/MM/YYYY:HH:MM:SS -0700] format
# %r - URI of request in double quotes
# %s - status code the server sent back
# %O - number of bytes sent
# ${Referer}i - request header with "Referer"
# ${User-agent}i - request header with "User-agent"

log_fields = ['client_ip', 'client_id', 'client_uid', 'timestamp', 'timeadjustment', 'uri', 'status', 'bytes_sent', 'referer', 'user-agent']



def log_entry_to_dict (log_entry):
    return {
    'client_ip': log_entry.split('"')[0].split()[0],
    'time_stamp': log_entry.split('"')[0].split()[3] + log_entry.split('"')[0].split()[4],
    'http_verb': log_entry.split('"')[1].split()[0],
    'request_uri': log_entry.split('"')[1].split()[1],
    'status_code': log_entry.split('"')[2].split()[0],
    'bytes_sent': log_entry.split('"')[2].split()[1],
    'user_agent': log_entry.split('"')[5]
    } 


def get_logs():
    with open('access.log') as file:
        raw_logs = file.readlines()
        return raw_logs


raw_logs = get_logs()

logs = []
for log_entry in raw_logs:
    logs.append(log_entry_to_dict(log_entry))

print([entry['client_ip'] for entry in logs if entry['status_code'] == '404'])
