"""
avl_transactions.py
This file contains the AVL Tree implementation for managing bank transactions.
"""

from datetime import datetime

class TransactionNode:
    def __init__(self, txn_id, amount, date):
        self.txn_id = txn_id
        self.amount = amount
        self.date = date
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, txn_id, amount, date):
        if not root:
            return TransactionNode(txn_id, amount, date)
        
        if txn_id < root.txn_id:
            root.left = self.insert(root.left, txn_id, amount, date)
        elif txn_id > root.txn_id:
            root.right = self.insert(root.right, txn_id, amount, date)
        else:
            root.amount = amount
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and txn_id < root.left.txn_id:
            return self.rotate_right(root)
        if balance < -1 and txn_id > root.right.txn_id:
            return self.rotate_left(root)
        if balance > 1 and txn_id > root.left.txn_id:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and txn_id < root.right.txn_id:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, txn_id):
        if not root or root.txn_id == txn_id:
            return root
        if txn_id < root.txn_id:
            return self.search(root.left, txn_id)
        return self.search(root.right, txn_id)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Transaction ID: {root.txn_id}, Amount: {root.amount}, Date: {root.date}")
            self.inorder(root.right)

    def get_total_balance(self, root):
        if not root:
            return 0
        return root.amount + self.get_total_balance(root.left) + self.get_total_balance(root.right)

    def search_by_date_range(self, root, start_date, end_date, result=[]):
        if root:
            txn_date = datetime.strptime(root.date, "%Y-%m-%d")
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")

            if start <= txn_date <= end:
                result.append((root.txn_id, root.amount, root.date))

            self.search_by_date_range(root.left, start_date, end_date, result)
            self.search_by_date_range(root.right, start_date, end_date, result)
        
        return result
