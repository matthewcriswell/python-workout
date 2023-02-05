from collections import Counter
#log_fields = ['client_ip', 'client_id', 'client_uid', 'timestamp', 'timeadjustment', 'uri', 'status', 'bytes_sent', 'referer', 'user-agent']


def log_entry_to_dict(log_entry):
    return {
        'client_ip':
        log_entry.split('"')[0].split()[0],
        'time_stamp':
        log_entry.split('"')[0].split()[3] +
        log_entry.split('"')[0].split()[4],
        'http_verb':
        log_entry.split('"')[1].split()[0],
        'request_uri':
        log_entry.split('"')[1].split()[1],
        'status_code':
        log_entry.split('"')[2].split()[0],
        'bytes_sent':
        log_entry.split('"')[2].split()[1],
        'user_agent':
        log_entry.split('"')[5]
    }


def get_logs():
    with open('access.log') as file:
        raw_logs = file.readlines()
        return raw_logs


raw_logs = get_logs()

logs = []
for log_entry in raw_logs:
    logs.append(log_entry_to_dict(log_entry))

statuscode_ip = {}
for i in set([int(entry['status_code']) for entry in logs]):
    statuscode_ip[i] = list(
        set([
            entry['client_ip'] for entry in logs
            if entry['status_code'] == str(i)
        ]))

print("")
print("IPs per requests:")
for status, clients in statuscode_ip.items():
    print(f"{status}: {clients}")

unique_ips = set()
for i in set([entry['client_ip'] for entry in logs]):
    unique_ips.add(i)

ip_req_status_counters = {}
# create a status_code count keyed off IP adddr and stuff in dict
for i in unique_ips:
    ip_req_status_counters[i] = Counter(
        [entry['status_code'] for entry in logs if entry['client_ip'] == i])

print("")
print("Requests per IP:")
for item in ip_req_status_counters.items():
    print(f"{item[0]}:", *item[1].items())

print("")
print("URIs per status code:")
for status_code in set([entry['status_code'] for entry in logs]):
    print(
        f"Status: {status_code} URIs:{set([entry['request_uri'] for entry in logs if entry['status_code'] == status_code])}"
    )
