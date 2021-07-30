
#/usr/bin/python3


from termcolor import colored ,cprint
import subprocess


#banner

b1= "██╗  ██╗ █████╗  ██████╗██╗  ██╗    ██████╗ ███████╗ ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ ███████╗██████╗" 
b2= "██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗"
b3= "███████║███████║██║     █████╔╝     ██║  ██║█████╗  ██║     ██║██████╔╝███████║█████╗  ██████╔╝█████╗  ██║  ██║"
b4= "██╔══██║██╔══██║██║     ██╔═██╗     ██║  ██║██╔══╝  ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗██╔══╝  ██║  ██║"
b5= "██║  ██║██║  ██║╚██████╗██║  ██╗    ██████╔╝███████╗╚██████╗██║██║     ██║  ██║███████╗██║  ██║███████╗██████╔╝"
b6= "╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ "

print("")
print("")
print("")
print_blue_on_green = lambda x: cprint(x, 'blue', 'on_green')
print_blue_on_green(b1)
print_blue_on_green(b2)
print_blue_on_green(b3)
print_blue_on_green(b4)
print_blue_on_green(b5)
print_blue_on_green(b6)

print("")
print('')
cprint("Owner :> @deciphered_nk -- Telegram ", 'magenta', attrs=['dark'])


#Community

print (" ")
print ("")
flw_1= " Follow us on YouTube   :- https://www.youtube.com/channel/UCcjlT-dqYMq_y1l1R3d4Oyg "
flw_2= " Follow us on Telegram  :- @Hack_Deciphered "

cprint(flw_1, 'red', attrs=['bold','blink'])
cprint(flw_2, 'red', attrs=['bold','blink'])
print("")

hrt="❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤"
print(hrt)
print("")
print("")

#Mac_Changer

net_intf1="[1] wlan0 (Wireless Connection)"
net_intf2="[2] eth0 (Wired Coteqnnection)"
cprint(net_intf1 , attrs=['bold'])
cprint(net_intf2 , attrs=['bold'])


intf=int(input("Select your Network Interface (1/2) : "))



if intf==1:
    mac_add=input("Enter a new Mac Address (Example- 00:78:12:12:12:12) :- ")
    subprocess.call(["ifconfig", "wlan0", "down"])
    subprocess.call(["ifconfig", "wlan0", "hw", "ether", mac_add ])
    subprocess.call(["ifconfig" , "wlan0", "up"])
    cprint("Your Mac Address changed Successfully!!😉😉", 'red', attrs=['bold','blink'])
    cprint("Follow us for More Tools and Techniques", 'red', attrs=['bold','blink'])

elif intf==2:
    mac_add=input("Enter a new Mac Address (Example- 00:78:12:12:12:12) :- ")
    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["ifconfig", "eth0", "hw","ether", mac_add ])
    subprocess.call(["ifconig" , "eth0", "up"])
    cprint("Your Mac Address changed Successfully!!😉😉", 'blue', attrs=['bold','blink'])
    cprint("Follow us for More Tools and Techniques", 'blue', attrs=['bold','blink'])
else:
    print("Choose The Correct Value (1/2)")
    cprint(net_intf1 , attrs=['bold'])
    cprint(net_intf2 , attrs=['bold'])
    intf=int(input("Select your Network Interface (1/2) : "))




