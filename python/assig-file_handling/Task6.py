{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a522319",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Ask user for 3 products and prices\n",
    "\n",
    "file = open(\"products.txt\", \"w\")\n",
    "\n",
    "for i in range(3):\n",
    "    product = input(\"Enter product name: \")\n",
    "    price = input(\"Enter price: \")\n",
    "\n",
    "    file.write(f\"{product} | {price}\\n\")\n",
    "\n",
    "file.close()\n",
    "\n",
    "\n",
    "# Read the file\n",
    "file = open(\"products.txt\", \"r\")\n",
    "\n",
    "for line in file:\n",
    "    print(line.strip())\n",
    "\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bfd2ec8",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"sdfg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f5cdd6f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "gen_ai (3.14.3.final.0)",
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
   "version": "3.14.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
