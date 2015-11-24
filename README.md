# Node Management

This is an example Ansible playbook for Freifunk node management.

It fetches the list of nodes from the Freifunk Düsseldorf map server and
executes a shell command on all of them. Of course, you won't have root access
on other nodes than your own. :)

To use it, first install Ansible. We had issues with IPv6 addresses as
hostnames in Ansible versions lower than 2.0, which is currently in beta. So
for now, you have to install the development version.

On OS X, use this line:

```shell
brew install ansible --HEAD
```

Next, the requirements. Make sure to *not*  use Python 3:

```shell
pip2.7 install -r requirements.txt
```

Now, you can execute the playbook like this:

```shell
ansible playbook.yml
```

The Linux distribution on the nodes is OpenWRT, packaged by the local Freifunk
people); so other Ansible modules than `raw` and `script` won't work.
Hopefully, someone will come up with a module for the `uci` management
interface.

Have fun and hack along!
