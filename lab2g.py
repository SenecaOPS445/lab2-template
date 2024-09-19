#!/usr/bin/env python3

#Author: Vitor Mendes Morita
#Author ID: vmmorita@myseneca.ca
#Date Created: 2024/9/4
#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    print("Error: Too many arguments provided.")
    sys.exit(1)

while timer > 0:
    print(timer)
    timer = timer - 1

print('blast off!')
