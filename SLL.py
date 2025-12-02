import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.address = self.generate_address()
    
    @staticmethod
    def generate_address():
        """Generate a fake memory address for visualization"""
        return f"0x{random.randint(0x1000, 0x9999):04X}"

class LinkedListVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Singly Linked List Visualizer - Pointer Edition")
        self.root.geometry("1400x800")
        self.root.configure(bg="#f0f0f0")
        
        self.head = None
        self.show_addresses = tk.BooleanVar(value=True)
        self.show_explanation = tk.BooleanVar(value=True)
        
        # Create main container
        container = tk.Frame(root, bg="#f0f0f0")
        container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left side - Visualization
        left_frame = tk.Frame(container, bg="#f0f0f0")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Title
        title_label = tk.Label(left_frame, text="Singly Linked List - Pointer Visualization", 
                               font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#2c3e50")
        title_label.pack(pady=5)
        
        # Options frame
        options_frame = tk.Frame(left_frame, bg="#f0f0f0")
        options_frame.pack(pady=5)
        
        tk.Checkbutton(options_frame, text="Show Memory Addresses", 
                      variable=self.show_addresses, command=self.draw_list,
                      font=("Arial", 10), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
        
        tk.Checkbutton(options_frame, text="Show Explanations", 
                      variable=self.show_explanation,
                      font=("Arial", 10), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
        
        # Canvas for visualization
        canvas_frame = tk.Frame(left_frame, bg="white", relief=tk.SUNKEN, bd=2)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add scrollbar to canvas
        canvas_scroll = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)
        canvas_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.canvas = tk.Canvas(canvas_frame, bg="white", height=350,
                               xscrollcommand=canvas_scroll.set)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas_scroll.config(command=self.canvas.xview)
        
        # Control panel
        control_frame = tk.Frame(left_frame, bg="#f0f0f0")
        control_frame.pack(fill=tk.X, pady=5)
        
        btn_config = {'font': ('Arial', 9, 'bold'), 'width': 15, 'height': 2}
        
        # Insert operations
        insert_frame = tk.LabelFrame(control_frame, text="Insert Operations", 
                                     font=("Arial", 10, "bold"), bg="#f0f0f0", fg="#27ae60")
        insert_frame.grid(row=0, column=0, padx=3, pady=3, sticky="ew")
        
        tk.Button(insert_frame, text="Insert at Beginning", command=self.beg_insert, 
                 bg="#2ecc71", fg="white", **btn_config).pack(side=tk.LEFT, padx=2, pady=3)
        tk.Button(insert_frame, text="Insert at End", command=self.last_insert, 
                 bg="#27ae60", fg="white", **btn_config).pack(side=tk.LEFT, padx=2, pady=3)
        tk.Button(insert_frame, text="Insert at Position", command=self.random_insert, 
                 bg="#229954", fg="white", **btn_config).pack(side=tk.LEFT, padx=2, pady=3)
        
        # Delete operations
        delete_frame = tk.LabelFrame(control_frame, text="Delete Operations", 
                                     font=("Arial", 10, "bold"), bg="#f0f0f0", fg="#c0392b")
        delete_frame.grid(row=1, column=0, padx=3, pady=3, sticky="ew")
        
        tk.Button(delete_frame, text="Delete from Beginning", command=self.begin_delete, 
                 bg="#e74c3c", fg="white", **btn_config).pack(side=tk.LEFT, padx=2, pady=3)
        tk.Button(delete_frame, text="Delete from End", command=self.last_delete, 
                 bg="#c0392b", fg="white", **btn_config).pack(side=tk.LEFT, padx=2, pady=3)
        tk.Button(delete_frame, text="Delete at Position", command=self.random_delete, 
                 bg="#a93226", fg="white", **btn_config).pack(side=tk.LEFT, padx=2, pady=3)
        
        # Utility operations
        utility_frame = tk.LabelFrame(control_frame, text="Utility Operations", 
                                      font=("Arial", 10, "bold"), bg="#f0f0f0", fg="#2980b9")
        utility_frame.grid(row=2, column=0, padx=3, pady=3, sticky="ew")
        
        tk.Button(utility_frame, text="Search Element", command=self.search, 
                 bg="#3498db", fg="white", **btn_config).pack(side=tk.LEFT, padx=2, pady=3)
        tk.Button(utility_frame, text="Clear All", command=self.clear_all, 
                 bg="#e67e22", fg="white", **btn_config).pack(side=tk.LEFT, padx=2, pady=3)
        
        # Info label
        self.info_label = tk.Label(left_frame, text="Ready! Pointers connect nodes together.", 
                                   font=("Arial", 10, "bold"), bg="#f0f0f0", fg="#34495e",
                                   wraplength=700, justify=tk.LEFT)
        self.info_label.pack(pady=5)
        
        # Right side - Explanation panel
        right_frame = tk.Frame(container, bg="#f0f0f0", width=350)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5)
        right_frame.pack_propagate(False)
        
        explanation_label = tk.Label(right_frame, text="📚 Pointer Explanation", 
                                    font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#2c3e50")
        explanation_label.pack(pady=5)
        
        self.explanation_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, 
                                                         font=("Courier", 9), 
                                                         bg="#ecf0f1", fg="#2c3e50",
                                                         relief=tk.SUNKEN, bd=2)
        self.explanation_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add pointer basics explanation
        self.show_pointer_basics()
        
        # Initial display
        self.draw_list()
    
    def show_pointer_basics(self):
        """Show basic pointer concepts"""
        basics = """
╔══════════════════════════════════╗
║   WHAT ARE POINTERS?             ║
╚══════════════════════════════════╝

A POINTER is a variable that stores 
the MEMORY ADDRESS of another variable.

In a Linked List:
• Each node has DATA + a POINTER
• The pointer "next" stores the 
  address of the next node
• HEAD pointer stores address of 
  first node
• Last node's pointer = NULL (nowhere)

╔══════════════════════════════════╗
║   POINTER VISUALIZATION          ║
╚══════════════════════════════════╝

[DATA | next] → means "next points to"

Memory addresses shown as 0x1234
(Simulated for learning)

╔══════════════════════════════════╗
║   TRY IT OUT!                    ║
╚══════════════════════════════════╝

1. Insert a few nodes
2. Watch how pointers connect them
3. See addresses change
4. Understand pointer manipulation!
"""
        self.explanation_text.insert("1.0", basics)
        self.explanation_text.config(state=tk.DISABLED)
    
    def update_explanation(self, operation, details):
        """Update explanation panel with current operation"""
        if not self.show_explanation.get():
            return
        
        self.explanation_text.config(state=tk.NORMAL)
        self.explanation_text.delete("1.0", tk.END)
        
        explanation = f"""
╔══════════════════════════════════╗
║   {operation.upper():^32} ║
╚══════════════════════════════════╝

{details}

╔══════════════════════════════════╗
║   KEY POINTER CONCEPTS           ║
╚══════════════════════════════════╝

• HEAD: Pointer to first node
• next: Pointer to next node  
• NULL: Pointer to nothing (end)
• Linking: Making a pointer point 
  to a node's address

Remember: Pointers store ADDRESSES,
not the actual data!
"""
        self.explanation_text.insert("1.0", explanation)
        self.explanation_text.config(state=tk.DISABLED)
    
    def draw_list(self, highlight_index=None, highlight_color="yellow"):
        """Draw the linked list with detailed pointer information"""
        self.canvas.delete("all")
        
        if self.head is None:
            self.canvas.create_text(400, 175, text="List is Empty\n\n☝️ Click 'Insert at Beginning' to add your first node!", 
                                   font=("Arial", 16, "bold"), fill="#95a5a6")
            self.canvas.config(scrollregion=(0, 0, 800, 400))
            return
        
        # Node dimensions
        node_width = 120
        node_height = 80
        arrow_length = 60
        start_x = 80
        start_y = 150
        
        current = self.head
        index = 0
        x = start_x
        max_x = x
        
        # Draw HEAD pointer with detail
        self.canvas.create_text(x - 30, start_y - 80, text="HEAD", 
                               font=("Arial", 14, "bold"), fill="#e74c3c")
        self.canvas.create_text(x - 30, start_y - 60, text="(pointer)", 
                               font=("Arial", 9), fill="#e74c3c")
        if self.show_addresses.get():
            self.canvas.create_text(x - 30, start_y - 45, text=f"{self.head.address}", 
                                   font=("Courier", 8), fill="#c0392b")
        
        # Draw arrow from HEAD to first node
        self.canvas.create_line(x - 30, start_y - 35, x + node_width//2, start_y - 10, 
                               arrow=tk.LAST, width=3, fill="#e74c3c")
        
        while current is not None:
            # Determine color
            if highlight_index is not None and index == highlight_index:
                fill_color = highlight_color
                text_color = "black"
                outline_color = "#f39c12"
                outline_width = 4
            else:
                fill_color = "#3498db"
                text_color = "white"
                outline_color = "#2c3e50"
                outline_width = 2
            
            # Draw memory address above node
            if self.show_addresses.get():
                self.canvas.create_text(x + node_width//2, start_y - 25, 
                                       text=f"Address: {current.address}", 
                                       font=("Courier", 9, "bold"), fill="#7f8c8d")
            
            # Draw node box
            self.canvas.create_rectangle(x, start_y, x + node_width, start_y + node_height, 
                                        fill=fill_color, outline=outline_color, width=outline_width)
            
            # Draw vertical divider (splits data and pointer sections)
            divider_x = x + node_width * 0.5
            self.canvas.create_line(divider_x, start_y, divider_x, start_y + node_height, 
                                   fill="white", width=3)
            
            # Draw data section label
            self.canvas.create_text(x + node_width * 0.25, start_y + 15, 
                                   text="data", font=("Arial", 8), fill="white")
            
            # Draw data value
            self.canvas.create_text(x + node_width * 0.25, start_y + node_height // 2 + 5, 
                                   text=str(current.data), font=("Arial", 16, "bold"), 
                                   fill=text_color)
            
            # Draw pointer section label
            self.canvas.create_text(x + node_width * 0.75, start_y + 15, 
                                   text="next", font=("Arial", 8), fill="white")
            
            # Draw index below node
            self.canvas.create_text(x + node_width // 2, start_y + node_height + 15, 
                                   text=f"Node {index}", font=("Arial", 10, "bold"), fill="#34495e")
            
            # Draw arrow/pointer to next node or NULL
            arrow_start_x = x + node_width
            arrow_start_y = start_y + node_height // 2
            
            if current.next is not None:
                # Draw pointer arrow with label
                arrow_end_x = x + node_width + arrow_length
                
                # Arrow
                self.canvas.create_line(arrow_start_x, arrow_start_y, 
                                       arrow_end_x, arrow_start_y, 
                                       arrow=tk.LAST, width=4, fill="#2ecc71")
                
                # Pointer symbol in the box
                self.canvas.create_text(x + node_width * 0.75, start_y + node_height // 2 + 5, 
                                       text="→", font=("Arial", 20, "bold"), fill="white")
                
                # Show what address it points to
                if self.show_addresses.get():
                    self.canvas.create_text(arrow_start_x + arrow_length//2, arrow_start_y - 20, 
                                           text=f"points to\n{current.next.address}", 
                                           font=("Courier", 7), fill="#27ae60")
                
                x += node_width + arrow_length
            else:
                # Draw NULL pointer
                self.canvas.create_text(x + node_width * 0.75, start_y + node_height // 2 + 5, 
                                       text="✗", font=("Arial", 20, "bold"), fill="#e74c3c")
                
                # NULL label outside
                self.canvas.create_text(x + node_width + 40, start_y + node_height // 2, 
                                       text="NULL\n(0x0000)", 
                                       font=("Arial", 11, "bold"), fill="#e74c3c")
                
                # Explanation
                self.canvas.create_text(x + node_width + 40, start_y + node_height // 2 + 35, 
                                       text="(End of list)", 
                                       font=("Arial", 8), fill="#95a5a6")
            
            max_x = max(max_x, x + node_width + 100)
            current = current.next
            index += 1
        
        # Update scroll region
        self.canvas.config(scrollregion=(0, 0, max_x, 400))
        self.root.update()
    
    def beg_insert(self):
        """Insert at the beginning with detailed explanation"""
        value = simpledialog.askinteger("Insert at Beginning", "Enter value:")
        if value is None:
            return
        
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        explanation = f"""
STEP-BY-STEP:

1. Create new node with data = {value}
   Address: {new_node.address}

2. Set new_node->next = HEAD
   (Point to current first node)
   {new_node.next.address if new_node.next else 'NULL'}

3. Update HEAD = new_node
   (HEAD now points to new node)

POINTER CHANGES:
• HEAD now points to: {self.head.address}
• New node's 'next' points to: 
  {new_node.next.address if new_node.next else 'NULL'}

This is O(1) - constant time!
Only HEAD pointer changed.
"""
        
        self.update_explanation(f"Insert {value} at Beginning", explanation)
        self.info_label.config(text=f"✅ Inserted {value} at beginning! HEAD pointer updated to point to new node.", 
                              fg="#27ae60")
        self.draw_list(highlight_index=0, highlight_color="#2ecc71")
    
    def last_insert(self):
        """Insert at the end with detailed explanation"""
        value = simpledialog.askinteger("Insert at End", "Enter value:")
        if value is None:
            return
        
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            explanation = f"""
STEP-BY-STEP:

1. Create new node with data = {value}
   Address: {new_node.address}

2. List is empty (HEAD = NULL)

3. Set HEAD = new_node
   (This becomes first node)

POINTER CHANGES:
• HEAD now points to: {self.head.address}
• New node's 'next' = NULL (last node)
"""
            self.update_explanation(f"Insert {value} (First Node)", explanation)
            self.info_label.config(text=f"✅ Inserted {value} as first node! HEAD points to it.", fg="#27ae60")
            self.draw_list(highlight_index=0, highlight_color="#2ecc71")
            return
        
        temp = self.head
        index = 0
        while temp.next is not None:
            temp = temp.next
            index += 1
        
        old_last_addr = temp.address
        temp.next = new_node
        
        explanation = f"""
STEP-BY-STEP:

1. Create new node with data = {value}
   Address: {new_node.address}

2. Traverse to last node
   Started at HEAD, moved {index} times
   
3. Found last node at: {old_last_addr}
   Its 'next' was NULL

4. Set last_node->next = new_node
   (Link last node to new node)

POINTER CHANGES:
• Old last node's 'next' now points to:
  {new_node.address}
• New node's 'next' = NULL (new last)

This is O(n) - must traverse entire list!
"""
        
        self.update_explanation(f"Insert {value} at End", explanation)
        self.info_label.config(text=f"✅ Inserted {value} at end! Traversed list and updated last node's pointer.", 
                              fg="#27ae60")
        self.draw_list(highlight_index=index + 1, highlight_color="#2ecc71")
    
    def random_insert(self):
        """Insert at a specific position"""
        value = simpledialog.askinteger("Insert at Position", "Enter value:")
        if value is None:
            return
        
        position = simpledialog.askinteger("Insert at Position", 
                                          "Enter position (0 for beginning):")
        if position is None:
            return
        
        new_node = Node(value)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            explanation = f"""
Position 0 = Insert at beginning!

POINTER CHANGES:
• new_node->next = HEAD
• HEAD = new_node
"""
            self.update_explanation(f"Insert {value} at Position {position}", explanation)
            self.info_label.config(text=f"✅ Inserted {value} at position {position}!", fg="#27ae60")
            self.draw_list(highlight_index=0, highlight_color="#2ecc71")
            return
        
        temp = self.head
        for i in range(position - 1):
            if temp is None:
                messagebox.showerror("Error", "Invalid position!")
                return
            temp = temp.next
        
        if temp is None:
            messagebox.showerror("Error", "Invalid position!")
            return
        
        prev_addr = temp.address
        new_node.next = temp.next
        next_addr = temp.next.address if temp.next else "NULL"
        temp.next = new_node
        
        explanation = f"""
STEP-BY-STEP:

1. Create new node: {new_node.address}

2. Traverse to position {position-1}
   Found node at: {prev_addr}

3. Set new_node->next = current->next
   New node points to: {next_addr}

4. Set current->next = new_node
   Previous node now points to: {new_node.address}

POINTER MANIPULATION:
• We "broke" the link between position
  {position-1} and {position}
• Inserted new node in between
• Re-established connections
"""
        
        self.update_explanation(f"Insert {value} at Position {position}", explanation)
        self.info_label.config(text=f"✅ Inserted {value} at position {position}! Pointers rearranged.", fg="#27ae60")
        self.draw_list(highlight_index=position, highlight_color="#2ecc71")
    
    def begin_delete(self):
        """Delete from beginning"""
        if self.head is None:
            messagebox.showwarning("Empty List", "List is empty!")
            return
        
        deleted_value = self.head.data
        deleted_addr = self.head.address
        new_head_addr = self.head.next.address if self.head.next else "NULL"
        
        self.head = self.head.next
        
        explanation = f"""
STEP-BY-STEP:

1. Save first node info:
   Data: {deleted_value}
   Address: {deleted_addr}

2. Move HEAD to next node:
   HEAD = HEAD->next
   New HEAD: {new_head_addr}

3. Free deleted node's memory
   (In C: free(ptr))

POINTER CHANGES:
• HEAD now points to: {new_head_addr}
• Old first node is disconnected
• Memory can be reclaimed

This is O(1) - just update HEAD!
"""
        
        self.update_explanation(f"Delete from Beginning", explanation)
        self.info_label.config(text=f"🗑️ Deleted {deleted_value} from beginning! HEAD moved to next node.", 
                              fg="#e74c3c")
        self.draw_list()
    
    def last_delete(self):
        """Delete from end"""
        if self.head is None:
            messagebox.showwarning("Empty List", "List is empty!")
            return
        
        if self.head.next is None:
            deleted_value = self.head.data
            deleted_addr = self.head.address
            self.head = None
            
            explanation = f"""
STEP-BY-STEP:

1. Only one node in list
   Address: {deleted_addr}

2. Set HEAD = NULL
   (List becomes empty)

3. Free the node

POINTER CHANGES:
• HEAD = NULL (empty list)
"""
            self.update_explanation(f"Delete Only Node", explanation)
            self.info_label.config(text=f"🗑️ Deleted {deleted_value} (only node)! List is now empty.", 
                                  fg="#e74c3c")
            self.draw_list()
            return
        
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next
        
        deleted_value = temp.data
        deleted_addr = temp.address
        prev_addr = prev.address
        
        prev.next = None
        
        explanation = f"""
STEP-BY-STEP:

1. Traverse to last node
   Last node: {deleted_addr}
   Previous node: {prev_addr}

2. Set previous->next = NULL
   (Break link to last node)

3. Free last node

POINTER CHANGES:
• Previous node's 'next' = NULL
  (It's now the last node)
• Old last node disconnected

This is O(n) - must traverse list!
"""
        
        self.update_explanation(f"Delete from End", explanation)
        self.info_label.config(text=f"🗑️ Deleted {deleted_value} from end! Second-to-last node now points to NULL.", 
                              fg="#e74c3c")
        self.draw_list()
    
    def random_delete(self):
        """Delete from specific position"""
        if self.head is None:
            messagebox.showwarning("Empty List", "List is empty!")
            return
        
        position = simpledialog.askinteger("Delete at Position", 
                                          "Enter position to delete (0 for first):")
        if position is None:
            return
        
        if position == 0:
            deleted_value = self.head.data
            self.head = self.head.next
            self.info_label.config(text=f"🗑️ Deleted {deleted_value} from position 0!", fg="#e74c3c")
            self.draw_list()
            return
        
        temp = self.head
        prev = None
        for i in range(position):
            if temp is None:
                messagebox.showerror("Error", "Invalid position!")
                return
            prev = temp
            temp = temp.next
        
        if temp is None:
            messagebox.showerror("Error", "Invalid position!")
            return
        
        deleted_value = temp.data
        deleted_addr = temp.address
        prev_addr = prev.address
        next_addr = temp.next.address if temp.next else "NULL"
        
        prev.next = temp.next
        
        explanation = f"""
STEP-BY-STEP:

1. Traverse to position {position}
   Node to delete: {deleted_addr}
   Previous node: {prev_addr}

2. Set previous->next = current->next
   Skip over deleted node
   Previous now points to: {next_addr}

3. Free deleted node

POINTER MANIPULATION:
• We "bypassed" the node at position {position}
• Previous node now links directly 
  to the next node
• Deleted node is disconnected
"""
        
        self.update_explanation(f"Delete from Position {position}", explanation)
        self.info_label.config(text=f"🗑️ Deleted {deleted_value} from position {position}! Pointers adjusted to skip it.", 
                              fg="#e74c3c")
        self.draw_list()
    
    def search(self):
        """Search for an element"""
        if self.head is None:
            messagebox.showwarning("Empty List", "List is empty!")
            return
        
        value = simpledialog.askinteger("Search", "Enter value to search:")
        if value is None:
            return
        
        temp = self.head
        index = 0
        addresses_checked = []
        
        while temp is not None:
            addresses_checked.append(temp.address)
            if temp.data == value:
                explanation = f"""
SEARCH PROCESS:

1. Start at HEAD: {self.head.address}

2. Follow 'next' pointers:
   Checked {index + 1} node(s)

3. Found {value} at position {index}!
   Address: {temp.address}

ADDRESSES CHECKED:
{chr(10).join(f"  • {addr}" for addr in addresses_checked)}

POINTER TRAVERSAL:
We followed the chain of 'next' pointers
from HEAD until we found the value!
"""
                self.update_explanation(f"Search Found: {value}", explanation)
                self.info_label.config(text=f"🔍 Found {value} at position {index}!", fg="#f39c12")
                self.draw_list(highlight_index=index, highlight_color="#f39c12")
                return
            temp = temp.next
            index += 1
        
        explanation = f"""
SEARCH PROCESS:

1. Started at HEAD: {self.head.address}

2. Followed 'next' pointers through
   entire list ({index} nodes)

3. Value {value} NOT found!

ADDRESSES CHECKED:
{chr(10).join(f"  • {addr}" for addr in addresses_checked)}

We traversed all pointers to NULL.
"""
        
        self.update_explanation(f"Search Not Found: {value}", explanation)
        messagebox.showinfo("Not Found", f"Value {value} not found in the list!")
        self.info_label.config(text=f"🔍 Value {value} not found after checking all nodes!", fg="#e74c3c")
    
    def clear_all(self):
        """Clear the entire list"""
        if messagebox.askyesno("Clear All", "Are you sure you want to clear the entire list?"):
            node_count = 0
            temp = self.head
            while temp:
                node_count += 1
                temp = temp.next
                
            self.head = None
            
            explanation = f"""
CLEARING LIST:

1. Set HEAD = NULL
   (Disconnect from list)

2. All {node_count} nodes are now unreachable

3. Memory will be freed
   (In C: iterate and free each node)

POINTER CONCEPT:
When HEAD = NULL and no other pointers
reference the nodes, they become
"garbage" and memory can be reclaimed.
"""
            self.update_explanation("Clear All Nodes", explanation)
            self.info_label.config(text=f"🗑️ List cleared! All {node_count} nodes removed, HEAD = NULL", fg="#e67e22")
            self.draw_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListVisualizer(root)
    root.mainloop()