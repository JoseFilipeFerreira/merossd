# 💡merossd
simple Meross webserver created to control all lights associated with a meross acount

## setup
* set `MEROSS_EMAIL` and `MEROSS_PASSWORD` envs
* ```./run.sh``` in the remote machine

## usage
|  endpoint    |  result            |
| ------------ | ------------------ |
| /bulb/       | get bulb status    |
| /bulb/on     | turn on all bulbs  |
| /bulb/off    | turn off all bulbs |
| /bulb/toggle | toggle all bulbs   |

## example scripts
* [meross-cli](https://github.com/JoseFilipeFerreira/toolbelt/blob/master/toolbox/meross-cli.tool) - control lights via terminal
* [toggle](https://github.com/JoseFilipeFerreira/shortcuts/blob/master/shorts/tasks/toggle) - control lights via [termux widget](https://wiki.termux.com/wiki/Termux:Widget)

## built with
* [Merossiot](https://github.com/albertogeniola/MerossIot)
* [Quart](https://pypi.org/project/Quart/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
