import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class BankDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking Management System")
        self.root.geometry("800x600")  # Window size

        self.accounts = {}  # Dictionary to store account details

        # Left Frame with Background Image
        self.left_frame = tk.Frame(self.root, bg="white", width=300, height=600)
        self.left_frame.pack(side="left", fill="y")
        self.left_image = Image.open("bank image.jpeg")  # the path of image
        self.left_image = self.left_image.resize((500, 600))
        self.left_image = ImageTk.PhotoImage(self.left_image)
        self.left_label = tk.Label(self.left_frame, image=self.left_image)
        self.left_label.pack(fill="both", expand=True)

        # Right Frame for Fields and Buttons
        self.right_frame = tk.Frame(self.root, bg="sky blue", width=500, height=600)  # Background color for the right frame
        self.right_frame.pack(side="right", expand=True, fill="both")


        # Title
        tk.Label(self.right_frame, text="Banking Management System", font=("Arial", 16, "bold"), bg="sky blue", fg="dark blue").pack(pady=20)

        # Input Fields
        tk.Label(self.right_frame, text="Name:", font=("Arial", 12), bg="light blue").pack(anchor="w", padx=20)
        self.name_entry = tk.Entry(self.right_frame, font=("Arial", 12))
        self.name_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.right_frame, text="Email ID:", font=("Arial", 12), bg="light blue").pack(anchor="w", padx=20)
        self.email_entry = tk.Entry(self.right_frame, font=("Arial", 12))
        self.email_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.right_frame, text="Account Number:", font=("Arial", 12), bg="light blue").pack(anchor="w", padx=20)
        self.account_entry = tk.Entry(self.right_frame, font=("Arial", 12))
        self.account_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.right_frame, text="IFSC Code:",font=("Arial", 12), bg="light blue").pack(anchor="w", padx=20)
        self.ifsc_entry = tk.Entry(self.right_frame, font=("Arial", 12))
        self.ifsc_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.right_frame, text="Contact Number:", font=("Arial", 12), bg="light blue").pack(anchor="w", padx=20)
        self.contact_entry = tk.Entry(self.right_frame, font=("Arial", 12))
        self.contact_entry.pack(fill="x", padx=20, pady=5)

        # Buttons
        button_create_account = tk.Button(self.right_frame, text="Create Account", font=("Arial", 12), bg="dark blue", fg="white", command=self.create_account)
        button_create_account.pack(pady=10, fill="x", padx=20)

        button_delete_account = tk.Button(self.right_frame, text="Delete Account", font=("Arial", 12), bg="red", fg="white", command=self.delete_account)
        button_delete_account.pack(pady=10, fill="x", padx=20)

        button_cancel = tk.Button(self.right_frame, text="Cancel", font=("Arial", 12), bg="grey", fg="white", command=self.cancel)
        button_cancel.pack(pady=10, fill="x", padx=20)

    def create_account(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        account_number = self.account_entry.get().strip()
        ifsc = self.ifsc_entry.get().strip()
        contact = self.contact_entry.get().strip()

        if not (name and email and account_number and ifsc and contact):
            messagebox.showerror("Error", "All fields are required!") # any fields are empty and shows the error msg
            return

        if account_number in self.accounts:
            messagebox.showerror("Error", "Account already exists!")  # account already exists
            return

        self.accounts[account_number] = {
            "Name": name,
            "Email": email,
            "IFSC": ifsc,
            "Contact": contact
        }

        messagebox.showinfo("Success", "Account created successfully!") # shows the success msg and clears the fields
        self.clear_fields()

    def delete_account(self):
        account_number = self.account_entry.get().strip()

        if not account_number:
            messagebox.showerror("Error", "Account number is required to delete!")
            return

        if account_number not in self.accounts:
            messagebox.showerror("Error", "Account does not exist!")
            return

        del self.accounts[account_number]
        messagebox.showinfo("Success", "Account deleted successfully!")
        self.clear_fields()

    def cancel(self):
        self.clear_fields()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.account_entry.delete(0, tk.END)
        self.ifsc_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = BankDetails(root)
    root.mainloop()
