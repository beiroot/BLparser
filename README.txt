WHAT?
This script is parsing any text looking for obfuscated bad IPs/domains.

WHY?
I created it because often bad ips/domains are somewhere inside a webpage, newsletter email etc. and getting it out, parsing and putting it all together was a pain.

HOW?
You can paste a text from a webpage, email, word document etc. and it will find the obfuscated ips/domains, delete unnecessary characters, sort IPs and domains and print it out to output.txt file.
Script outputs a list in alphabetical order, that is IP are always first, domains go next. It also takes care of all unicode and non-ascii characters.

The script takes one argument -f FILE
FILE is the input file.
You can omit the argument, but there has to be "input.txt" file in the same folder as the script.

Output will always be output.txt

input
FILE: input.txt
101[.]99[.]75[.]151
dns1[.]soprodns[.]ru
makewebomb[.]xyz
gandcrab(.)bit
test(.)nomoreransom(.)bit
101(.)99(.)75(.)151
hxxp://nomoreransom[.]coin
hxxp://ipv4bot[.]whatismyipaddress(.)com
hxxps://nomoreransom[.]co
hxxps://ipv6bot(.)whatismyipaddress[.]com

output:
FILE: output.txt
101.99.75.151
101.99.75.151
dns1.soprodns.ru
gandcrab.bit
http://ipv4bot.whatismyipaddress.com- (added "-" manually so that you don't accidentally click it. better safe than sorry :))
http://nomoreransom.coin-
https://ipv6bot.whatismyipaddress.com-
https://nomoreransom.co-
makewebomb.xyz
test.nomoreransom.bit


!!! If the domain starts with a number it may appear on IPs list, but fixing that would make the script
       unnecessarily complicated.

 
