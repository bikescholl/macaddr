# MAC Address Exercise

This was a fun little exercise around querying an API in python using standard request calls. It leverages docker to run the scripts with appropriate vairables.

### Prerequisites

Docker must be installed and running on your system in order for this to work. It must also be able to pull from docker.io.

In addition these Docker containers run under certain users to prevent root system level access within the container. It's also assumed that the user running these builds has the ability to run docker under the sudo context.

### Installing

To build the Docker containers to operate this command line tool you can run the built in Makefile. This uses a built in API key. 

```
make image
```

Alternatively it is recommended you use your own API key when attempting to run this by running the Docker build manually.

```
sudo docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} . --build-args API_KEY=${API_KEY}
```

### Usage

To run the docker container you must feed a valid MAC address to the command line via `docker run`. It's default output is formatted JSON information about the vendor.

```
sudo docker run -ti mac_lookup:1.0.0 44:38:39:ff:ef:57
```

There are additional flags that can be specified if you want YAML and JSON full details about the MAC Address

```
sudo docker run -ti mac_lookup:1.0.0 44:38:39:ff:ef:57 --yaml
```

```
sudo docker run -ti mac_lookup:1.0.0 44:38:39:ff:ef:57 --json
```


### Tests

As a fun little exercise I've added a linter test to validate the Python3 code within the /scripts/mac_addr_lookup.py script. You can run the tests via the Makefile

```
make lint
```

### Authors

* **Mike Scholl** - *Initial work and builds*

See also the list of [contributors](https://github.com/mgs4332/macaddr/graphs/contributors) who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

