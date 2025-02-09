# python_keylogger🔍⌨️  

This Python script logs **keyboard activity** in the background and sends the captured keystrokes to a remote server via an HTTP POST request. It also saves the keystrokes locally in a text file for tracking.  

## **Features 🚀**  
✅ Captures **all keyboard events** (letters, numbers, special keys).  
✅ Logs keystrokes into a **local file (`keylogs.txt`)**.  
✅ **Sends keystrokes** to a remote server periodically.  
✅ Uses **multi-threading** for efficient background execution.  
✅ **Stops monitoring when `ESC` is pressed**.  

## **How It Works 🔧**  
1. **Listens** for key events using `pynput`.  
2. **Stores keystrokes** in memory and appends them to `keylogs.txt`.  
3. **Sends data** to a remote server (`http://<server-ip>:8080`) using `requests.post()`.  
4. Runs in the background and **stops when `ESC` is pressed**.  

## **Installation & Setup 🛠️**  

### **1️⃣ Install Dependencies**  
```bash
pip install pynput requests
```

### **2️⃣ Run the Script**  
```bash
python keylogger.py
```

### **3️⃣ Start the Server (Python HTTP Server)**  
On your remote server, run:  
```bash
python server.py
```
> *(Use the provided `server.py` script in this repo to handle incoming data.)*  

## **Usage 🖥️**  
- Press **any key**, and it will be logged.  
- **Press `ESC` to stop monitoring**.  
- Check `keylogs.txt` for recorded keystrokes.  
- View received keystrokes on the **server logs**.  

## **Example Server Response (Flask Version) 🖧**  
```json
{
  "status": "success"
}
```

## **Notes ⚠️**  
- Ensure your **server IP and port** are correctly set.  
- Run the script with **admin/root privileges** if needed.  
- **This tool is for educational & ethical use only**. 🚫  

---

Would you like me to format it further or add a **README.md** file for your repo? 🚀
