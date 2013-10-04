from ubuntu:12.10

maintainer Nick Stinemates

run apt-get install -y software-properties-common
run add-apt-repository -y ppa:rethinkdb/ppa
run apt-get update
run apt-get install -y rethinkdb

expose 8080
expose 28015


cmd ["rethinkdb", "--bind", "all"]
