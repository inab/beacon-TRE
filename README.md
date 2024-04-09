# Beacon TRE

This repository has the [Reference Implementation Beacon](https://github.com/GenomicDataInfrastructure/starter-kit-beacon2-ri-api) from [GDI](https://gdi.onemilliongenomes.eu/) that works with [RabbitMQ](https://www.rabbitmq.com/) for Trusted Research Environments (TREs).

## Before Running

You can create a Python environment in the [starter-kit-beacon2-ri-api](starter-kit-beacon2-ri-api) folder

# Usage

To run the full environment you will need at least 2 terminals running. One for the beacon client and other for the RabbitMQ client.

## Open RabbitMQ

- Run RabbitMQ with docker, add `-d` to run it in the background: 
 
 ```
 # latest RabbitMQ 3.13
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
 ```

- Run the RabbitMQ script to query internally your desired beacon:

```
python3 rpc_beacon_server.py https://beacons.bsc.es/beacon-network/v2.0.0/

```
In the first argument you must put the beacon inside your server that you want to query. Meanwhile all the other servers are running you can close and run again this script with a new beacon.

## Run Beacon TRE

This Beacon will be the one sending and receiving messages from RabbitMQ. The query from the user will be the input message in RabbitMQ and the message that it will receive from the RabbitMQ will be the Beacon response.

- Run the Beacon TRE:

```
cd starter-kit-beacon2-ri-api
python -m beacon
```

Congrats! You have deployed the Beacon TRE in [http://localhost:5050/api](http://localhost:5050/api).
