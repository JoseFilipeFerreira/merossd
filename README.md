# merossd
simple Meross daemon 

## setup
* install [meross_iot](https://github.com/albertogeniola/MerossIot)
* set `MEROSS_EMAIL` and `MEROSS_PASSWORD` envs

## usage
* write to the pipe `/tmp/meross.d` to change the state
| input  | result             |
|--------|--------------------|
| on     | turn on all bulbs  |
| off    | turn off all bulbs |
| toggle | toggle all bulbs   |
| close  | close deamon       |

* read from the pipe `/tmp/merossstate.d` to get the state of all bulbs

## example scripts
*[meross-cli](https://github.com/JoseFilipeFerreira/toolbelt/blob/master/toolbox/meross-cli.tool)

## built with
* [Merossiot](https://github.com/albertogeniola/MerossIot)
*
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
