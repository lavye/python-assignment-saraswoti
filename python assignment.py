{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bd4bf408-a1c4-4d3d-bd11-189631107fd9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1) Write a Python program that simulates a basic calculator, performing addition, subtraction, \n",
    "#multiplication, and division. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8a7f354b-3132-4c50-bee8-4ed482b2afad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "choose operation:+,-,*,/\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "operation: /\n",
      "First number: 24\n",
      "second number: 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 3.0\n"
     ]
    }
   ],
   "source": [
    "print(\"choose operation:+,-,*,/\")\n",
    "op=input(\"operation:\")\n",
    "num1=float(input(\"First number:\"))\n",
    "num2=float(input(\"second number:\"))\n",
    "if op == '+':\n",
    "    print(\"Result:\", num1 + num2)\n",
    "elif op == '-':\n",
    "    print(\"Result:\", num1 - num2)\n",
    "elif op == '*':\n",
    "    print(\"Result:\", num1 * num2)\n",
    "elif op == '/':\n",
    "    if num2 != 0:\n",
    "        print(\"Result:\", num1 / num2)\n",
    "    else:\n",
    "        print(\"Error: Cannot divide by zero\")\n",
    "else:\n",
    "    print(\"Invalid operation\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0949d81-467e-45cb-8a17-d73f2715056c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2) Decimal to Binary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d6e31775-0fbb-4536-885c-8c2e18aedf87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a decimal number:  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Binary equivalent: 110\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a decimal number: \"))\n",
    "print(\"Binary equivalent:\", bin(num)[2:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94f6cff4-f447-4f02-a647-ab050cf45604",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3) Age Category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f33bbe73-55c0-447a-a3f7-984de4c02c13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age:  18\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are an adult.\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"Enter your age: \"))\n",
    "if age < 18:\n",
    "    print(\"You are a minor.\")\n",
    "elif age < 60:\n",
    "    print(\"You are an adult.\")\n",
    "else:\n",
    "    print(\"You are a senior.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37b10013-2ce5-4abf-9ab0-1ca1023aab10",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4) Swap without third variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3c642cee-9c3f-4ee2-be09-c7d72939be63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  34\n",
      "Enter second number:  23\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Swapped values: 23 34\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter first number: \"))\n",
    "b = int(input(\"Enter second number: \"))\n",
    "a, b = b, a\n",
    "print(\"Swapped values:\", a, b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e41da3cb-b5ed-4927-a389-2ff3b7b0649c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5) Fibonacci (first 10 numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a06f0d98-3e53-4fb2-a5d7-ccd2bfd31abf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 1 2 3 5 8 13 21 34 "
     ]
    }
   ],
   "source": [
    "a, b = 0, 1\n",
    "for _ in range(10):\n",
    "    print(a, end=' ')\n",
    "    a, b = b, a + b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef341f03-fbad-4ba1-80f1-a61dcf0cb1ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 6) Prime Number Check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "318e5b39-c174-40e5-8857-3ac9aca4b2f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Enter a number:  24\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Not Prime\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"\\nEnter a number: \"))\n",
    "if n > 1:\n",
    "    for i in range(2, n):\n",
    "        if n % i == 0:\n",
    "            print(\"Not Prime\")\n",
    "            break\n",
    "    else:\n",
    "        print(\"Prime\")\n",
    "else:\n",
    "    print(\"Not Prime\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08413cd2-2031-4fd9-b312-a22ffcebe667",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 7) Check Sum with Logical Operators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5d6e08fb-1810-4ac8-99de-9d730d53645a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  4\n",
      "Enter second number:  9\n",
      "Enter third number:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Third is sum of first two: False\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter first number: \"))\n",
    "b = int(input(\"Enter second number: \"))\n",
    "c = int(input(\"Enter third number: \"))\n",
    "print(\"Third is sum of first two:\", c == (a + b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "587dc898-11d5-4698-a39f-88136dfac636",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 8) Custom factorial module"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "bb1a8f24-783d-42b5-b190-87aa959cbd8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number to find factorial:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial: 24\n"
     ]
    }
   ],
   "source": [
    "import factorial_module\n",
    "\n",
    "num = int(input(\"Enter number to find factorial: \"))\n",
    "print(\"Factorial:\", factorial_module.factorial(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be62f52b-bb25-4b83-9a7e-19396bced6e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 9) Division with zero check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1aa81cc5-6070-4bb5-baeb-66b8ceb03ed6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter numerator:  45\n",
      "Enter denominator:  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Division by zero is not allowed.\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter numerator: \"))\n",
    "b = int(input(\"Enter denominator: \"))\n",
    "if b != 0:\n",
    "    print(\"Result:\", a / b)\n",
    "else:\n",
    "    print(\"Division by zero is not allowed.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec9a0a9a-5b0e-4d31-9fe0-915284b659d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 10) Max in List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f9cf634f-d810-4a98-ae98-2aa7f2bcefe7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter numbers separated by space:  4 5 3 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum value: 9\n"
     ]
    }
   ],
   "source": [
    "def find_max(numbers):\n",
    "    if not numbers:\n",
    "        return \"List is empty\"\n",
    "    max_val = numbers[0]\n",
    "    for num in numbers:\n",
    "        if num > max_val:\n",
    "            max_val = num\n",
    "    return max_val\n",
    "nums = list(map(int, input(\"Enter numbers separated by space: \").split()))\n",
    "print(\"Maximum value:\", find_max(nums))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d6401e6-b83f-41fe-8695-9115df54ba22",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 11) Greeting with default age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7a2982b3-a6fe-4259-a7fd-c427992ac1dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello,Alice! You are 25 years old.\n",
      "Hello,Ray! You are 30 years old.\n"
     ]
    }
   ],
   "source": [
    "def greet(name,age=25):\n",
    "    print(f\"Hello,{name}! You are {age} years old.\")\n",
    "    \n",
    "greet(\"Alice\")   \n",
    "greet(\"Ray\", 30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7e75076f-1fba-4e26-8691-412bbe7e8bbd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string:  paradise\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of vowels: 4\n"
     ]
    }
   ],
   "source": [
    "# 12) count the number of vowels in a string\n",
    "def count_vowels(text):\n",
    "    vowels = 'aeiouAEIOU'\n",
    "    count = 0\n",
    "    for char in text:\n",
    "        if char in vowels:\n",
    "            count += 1\n",
    "    return count\n",
    "string = input(\"Enter a string: \")\n",
    "print(\"Number of vowels:\", count_vowels(string))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1d2427ad-f575-40dc-bc60-97d760217061",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Multiplication Table for 10\n",
      "10 x 1 = 10\n",
      "10 x 2 = 20\n",
      "10 x 3 = 30\n",
      "10 x 4 = 40\n",
      "10 x 5 = 50\n",
      "10 x 6 = 60\n",
      "10 x 7 = 70\n",
      "10 x 8 = 80\n",
      "10 x 9 = 90\n",
      "10 x 10 = 100\n"
     ]
    }
   ],
   "source": [
    "# 13) Multiplication table up to (number × 10)\n",
    "num = int(input(\"Enter a number: \"))\n",
    "print(f\"Multiplication Table for {num}\")\n",
    "for i in range(1, 11):\n",
    "    print(f\"{num} x {i} = {num * i}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "00b7ae12-72b3-4ae9-a3e1-1931300da69d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number of rows:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*\n",
      "**\n",
      "***\n",
      "****\n",
      "*****\n"
     ]
    }
   ],
   "source": [
    "# 14) Right-angled triangle pattern\n",
    "rows = int(input(\"Enter number of rows: \"))\n",
    "for i in range(1, rows + 1):\n",
    "    print('*' * i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "16df10e1-55d4-4154-86a2-15dd3eb07ce6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter number of rows:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    *\n",
      "   ***\n",
      "  *****\n",
      " *******\n",
      "*********\n"
     ]
    }
   ],
   "source": [
    "# 15) Pyramid pattern\n",
    "rows = int(input(\"Enter number of rows: \"))\n",
    "for i in range(1, rows + 1):\n",
    "    spaces = ' ' * (rows - i)\n",
    "    stars = '*' * (2 * i - 1)\n",
    "    print(spaces + stars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "51bdc8ea-4d8b-49e4-910d-72bd5456b553",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# 1) Palindrome number\n",
    "def is_palindrome(x):\n",
    "    return str(x) == str(x)[::-1]\n",
    "print(is_palindrome(121)) \n",
    "print(is_palindrome(123)) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8ed5a334-0e67-455e-8759-6ecc47933355",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "# 2) Single number\n",
    "nums = [2, 3, 5, 2, 3]\n",
    "for num in nums:\n",
    "    if nums.count(num) == 1:\n",
    "        print(num)\n",
    "        break "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ad4ef505-8dc6-4b23-a326-46618c3fcf54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1\n"
     ]
    }
   ],
   "source": [
    "# 3) Two sum\n",
    "nums = [2, 7, 11, 15]\n",
    "target = 9\n",
    "\n",
    "for i in range(len(nums)):\n",
    "    for j in range(i + 1, len(nums)):\n",
    "        if nums[i] + nums[j] == target:\n",
    "            print(i, j)\n",
    "            break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3f7cafd1-3827-4a48-8750-3792c9a7d365",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "# 4) Happy Number\n",
    "def is_happy(n):\n",
    "    seen = set()\n",
    "    while n != 1 and n not in seen:\n",
    "        seen.add(n)\n",
    "        n = sum(int(digit) ** 2 for digit in str(n))\n",
    "    return n == 1\n",
    "print(is_happy(19))  # True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2fb0e5cd-21e2-406d-ba10-77efda5e72ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# 5)Duplicate number\n",
    "def contains_duplicate(nums):\n",
    "    return len(nums) != len(set(nums))\n",
    "print(contains_duplicate([1, 2, 3, 1]))  \n",
    "print(contains_duplicate([1, 2, 3]))   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff7ff5ab-5353-4733-9ec2-b42b71e41e28",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
