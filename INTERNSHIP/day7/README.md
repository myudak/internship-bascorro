# DAY 7 RANGKUMAN STUDY NOTES BASCORRO INTERNSHIP

11/21/2024

### APA ITU EPOCH

epoch artinya semuah model sudah melihat/mempelajari satu full dataset sekali

analoginya seperti kayak baca buku, baca buku dari start sampai akhir itu seperti satu epoch

nge train data sering kali banyak epoch kayak 50 sampai 100, karena sekali pass (one pass) tidak cukup untuk mempelajari semua pattern dalam data

When training a model like YOLO, **epoch**, **batch**, and other parameters are crucial for controlling how the model learns. Here’s an ELI5 explanation of each term:

### **1. Epoch**

- **What is it?**  
  An epoch means the model has gone through the **entire training dataset** once.
- **Analogy:** Imagine you’re reading a book. Going through the whole book from start to finish one time is like one epoch.
- **In training:** We often train for many epochs (e.g., 50 or 100) because one pass isn’t enough to learn all the patterns in the data.

---

### **2. Batch**

- **What is it?**  
  Instead of processing the whole dataset at once (which can be slow and require a lot of memory), the data is split into smaller chunks called **batches**.
- **Analogy:** If your book has 100 pages and you read 10 pages at a time, each set of 10 pages is a batch.
- **In training:** The model processes one batch, updates itself (via backpropagation), and then moves to the next batch.

---

### **3. Batch Size**

- **What is it?**  
  This defines how many data samples are in each batch.
- **Small batch size (e.g., 8):**
  - Slower training but uses less memory.
  - Might lead to better generalization.
- **Large batch size (e.g., 64):**
  - Faster training but uses more memory.
  - Can sometimes overfit.

---

### **4. Learning Rate**

- **What is it?**  
  This controls how big the "steps" are when the model updates itself after processing each batch.
- **Analogy:** If you’re climbing a hill, the learning rate is how big your steps are.
  - **Too big:** You might overshoot the top.
  - **Too small:** It will take forever to reach the top.

---

### **5. Iteration**

- **What is it?**  
  An iteration happens each time the model processes one batch.
- **Relationship with epochs:**
  - If you have 1000 samples and a batch size of 100, one epoch will have **10 iterations** (1000 ÷ 100 = 10).

---

### In YOLO Training:

- **Epochs:** Control how many times the model sees the entire dataset (e.g., 50–300 epochs are common).
- **Batch Size:** Balances memory use and speed. For YOLO, smaller batches (e.g., 16 or 32) are often used because YOLO models are memory-intensive.
- **Learning Rate:** Needs to be tuned carefully; YOLO often uses a **learning rate schedule** to start large and decrease gradually.

These parameters all work together to make training efficient and ensure the YOLO model learns effectively.
