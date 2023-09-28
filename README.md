## InfluxDB and Mage.ai for downsampling tasks 

This project uses Mage to create a downsampling pipeline that runs on a schedule. 

## How to run

1. Clone this directory
2. Get a database, token, and InfluxDB URL after signing up for a [free trial](https://cloud2.influxdata.com/signup). 
3. Write configure a [telegraf agent to write cpu data](https://www.influxdata.com/blog/tldr-influxdb-tech-tips-creating-telegraf-configuration-influxdb-ui/). 
4. Run the following command:
```
docker run -it \
           -p 6789:6789 \
           -e "TOKEN=<your token>" \
           -e "DATABASE=<your database>" \
           -e "HOST=<your url i.e. us-east-1-1.aws.cloud2.influxdata.com>" \
           -v "$(pwd):/home/src" \
           mageai/mageai \
           /app/run_app.sh mage start influxdb
```
1. Navigate to localhost:6789
2. Install the `influxdb3-python` requirement. From the requirements.txt file. Navigate to **Pipelines>broken_fog>Edit** through the Mage UI and click **Install Packages**