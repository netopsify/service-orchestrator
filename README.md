# End To End Service Orchestrator

This is an example demonstration of building and deploying configuration on the following:

1. User will request a new service either via csv file or Jira ticket.
2. The request will be modeled to the right format based on the service. e.g this example is deploying Virtual Servers on F5 devices hence it will be modeled based on that.
3. Source of Truth will be updated based on the request. (Right now its updating host vars however this can be easily expanded to updating any other system.)
4. Source of Truth data will be used to create service models.
5. Service models will be used to create and/or Deploy configuration on device.

The current demonstration is for generating F5 `tmsh` based commands. However this model can be extended easily to other platforms.
The idea here is to demonstrate the staged logic of receiving the request and generating an automation pipeline to deploy it ultimately.

The example below is a manual run for CSV input. However the a running Jira instance can be used too.
In real word scenario the csv can be placed in a git repository and can have a pipeline set for this automation process.

## Example

### Generating/Deploying Config for creating VIP on F5 devices using CSV

- Fill in the CSV file located at `user_request/request_csv` Or Provide Jira story URL with subtasks. Fill the variables in `group_vars/all` The Jira input assumes certain input standard. i.e. The summary and description fields of the ticket should follow a standard text format.
- For filling the CSV the following rules must be followed.
  - All fields are necessary.
  - The role will identify every VIP with its unique `vip_name` and `vip_port`. So those two are supposed to be unique.
  - Each line represents a VIP with one pool member and type. If you have more than one pool member, which will be most of the time, then you need to copy the same line twice and change the `node_name`, `node_ip` and `node_port` information.

### Run the playbook

Run the ansible playbook with two below options.

#### To run with CSV INPUT

```bash
ansible-playbook pb_config_generator.yml \
    -i "localhost" -c "local" \
    -e "platform=f5" \
    -e "email_from=user@netopsify.net" \
    -e "email_to=user@netopsify.net" \
    -e "csv_input=True" \
    --ask-vault-pass
```

#### To run with Jira INPUT

```bash
ansible-playbook pb_config_generator.yml \
    -i "localhost" -c "local" \
    -e "platform=f5" \
    -e "email_from=user@netopsify.net" \
    -e "email_to=user@netopsify.net" \
    -e "jira_input=True" \
    -e "jira_url=http://192.168.100.100:8001/browse/NLBR-2" \
    --ask-vault-pass
```
