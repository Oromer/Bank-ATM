{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Little steps towards progress'''\n",
    "\n",
    "'''\n",
    "Bank acocunt with two attributes; Name & Balance.\n",
    "One can Deposit & Withdraw from it.\n",
    "Be carefull though, cash aint limitless!!\n",
    "'''\n",
    "\n",
    "class Account:\n",
    "    \n",
    "    def __init__(self,name,balance):\n",
    "        self.name = name\n",
    "        self.balance = balance\n",
    "        \n",
    "    def __str__(self):\n",
    "        return (f'Name: {self.name} \\nBalance: {self.balance}')\n",
    "        \n",
    "    def deposit(self,deposit_amount):\n",
    "        self.balance += deposit_amount\n",
    "        print('Deposit accepted')\n",
    "        \n",
    "    def withdraw(self,withdraw_amount):\n",
    "        if self.balance >= withdraw_amount:\n",
    "            self.balance -= withdraw_amount\n",
    "            print('Withdraw accepted')\n",
    "        else:\n",
    "            print('Insufficient funds')\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Adding an account for Jose and an initial deposit of 100          \n",
    "acctjose= Account('Jose',100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Jose \n",
      "Balance: 100\n"
     ]
    }
   ],
   "source": [
    "#Let check it out on screen\n",
    "print(acctjose)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Jose'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Who's account?\n",
    "acctjose.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#How much in it?\n",
    "acctjose.balance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Deposit accepted\n"
     ]
    }
   ],
   "source": [
    "#Lets deposit some money\n",
    "acctjose.deposit(50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "150"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Was the money deposited?\n",
    "acctjose.balance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Withdraw accepted\n"
     ]
    }
   ],
   "source": [
    "#Lets withdraw that money out!!\n",
    "acctjose.withdraw(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Was the money withdrawn?\n",
    "acctjose.balance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Insufficient funds\n"
     ]
    }
   ],
   "source": [
    "#Lets take out 1000\n",
    "acctjose.withdraw(1000)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
