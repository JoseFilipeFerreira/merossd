# 💡merossd
simple Meross daemon created to control all lights associated with a meross acount from the terminal

## setup
* set `MEROSS_EMAIL` and `MEROSS_PASSWORD` envs
* ```./run.sh``` in the remote machine

## usage
* write to the pipe `/tmp/meross.d` to change the state

|  input  |  result             |
| ------- | ------------------- |
| on      | turn on all bulbs   |
| off     | turn off all bulbs  |
| toggle  | toggle all bulbs    |
| close   | close deamon        |

* read from the pipe `/tmp/merossstate.d` to get the state of all bulbs

## example scripts
the following scripts assume that the daemon is running on a remote machine 
* [meross-cli](https://github.com/JoseFilipeFerreira/toolbelt/blob/master/toolbox/meross-cli.tool) - control lights via terminal
* [toggle](https://github.com/JoseFilipeFerreira/shortcuts/blob/master/shorts/tasks/toggle) - control lights via [termux widget](https://wiki.termux.com/wiki/Termux:Widget)

## built with
* [Merossiot](https://github.com/albertogeniola/MerossIot)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
