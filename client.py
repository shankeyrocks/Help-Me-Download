import asyncore
import socket
import time
import thread
from time import *
import threading, urllib2,urllib
import Queue
import sys
from Tkinter import *
import tkFileDialog, Tkconstants
import os
import ttk
from urllib2 import Request, HTTPError, URLError
import httplib
import tkMessageBox

no_of_connections=0
no_of_acceptance=0
start_flag = False;
connect_flag = False;

win = Tk()

def run_thread(a) :
    asyncore.loop()








class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue


        # Set up the GUI
        #Tkinter.Frame.__init__(self, master)

        # options for buttons
        #button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        """
        self.L1 = Label(master, text="URL")
        self.L1.grid( row=0, column=0, sticky = W, padx=10, pady=10)
        
        self.E1 = Entry(master, bd =5,width=50)
        self.E1.grid( row=0, column=1, columnspan = 1, padx=10, pady=10)
        
        self.L2 = Label(master, text="Destination path")
        self.L2.grid( row=1, column=0, sticky = W, padx=10, pady=10)

        self.v = StringVar()
        self.E2 = Entry(master, bd =5,textvariable=self.v,width=50)
        self.E2.grid( row=1, column=1, padx=2, pady=10)
        
        self.B1=Button(master, text='Browse', command=self.askdirectory,bd=2)
        self.B1.grid( row=1, column=2, padx=6, pady=0, sticky= E )

        self.L3 = Label(master, text="Available Clients")
        self.L3.grid( row=2, column=0, sticky = W, padx=10, pady=10)
      
        

        self.Li1= Listbox(master,width=50,selectmode=MULTIPLE,height=4)
        self.Li1.grid( row=2, column=1, sticky = W,columnspan = 1, padx=10, pady=10)
        self.Li1.insert(1, "Python")
        self.Li1.insert(2, "Perl")
        self.Li1.insert(3, "C")
        self.Li1.insert(4, "PHP")
        self.Li1.insert(5, "JSP")
        self.Li1.insert(6, "Ruby")
        

        self.s = ttk.Scrollbar(master, orient=VERTICAL, command=(self.Li1).yview)
        self.s.grid(column=2, row=2, sticky=(W,N,S))
        self.Li1['yscrollcommand'] = self.s.set
        #ttk.Sizegrip().grid(column=2, row=2, sticky=(S,E))
       

        self.B2=Button(master, text='Connect')
        self.B2.grid( row=3, column=1, padx=4, pady=10 )


        self.L4 = Label(master, text="Connected Clients")
        self.L4.grid( row=4, column=0, sticky = W, padx=10, pady=10)
        

        self.Li2= Listbox(master,width=50,height=4)
        self.Li2.grid( row=4, column=1, sticky = W,columnspan = 1, padx=10, pady=10)
        self.Li2.insert(1, "Python")
        self.Li2.insert(2, "Perl")
        self.Li2.insert(3, "C")
        self.Li2.insert(4, "PHP")
        self.Li2.insert(5, "JSP")
        self.Li2.insert(6, "Ruby")

        self.s1 = ttk.Scrollbar(master, orient=VERTICAL, command=(self.Li2).yview)
        self.s1.grid(column=2, row=4, sticky=(W,N,S))
        self.Li2['yscrollcommand'] = self.s1.set
        #ttk.Sizegrip().grid(column=2, row=4, sticky=(S,E))

        self.B3=Button(master, text='Start Download',command=self.start)
        self.B3.grid( row=5, column=1, padx=4, pady=10 )


        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'Select Location:'

        self.progress = ttk.Progressbar(master, orient="horizontal", 
                                        length=200, mode="determinate")
        self.progress.grid(row=6, column=1, padx=4, pady=10)

        self.bytes = 0
        self.maxbytes = 0
        self.master=master
        #self.endCommand=endCommand


        """

        self.L1 = Label(master, text="URL")
        self.L1.grid( row=0, column=0, sticky = W, padx=10, pady=10)

        self.urlentered = StringVar()
        self.urlbox = Entry(master,textvariable=self.urlentered,bd=5,width=50)
        self.urlbox.grid( row=0, column=1, padx=2, pady=10)

        self.L2 = Label(master, text="Destination path")
        self.L2.grid( row=1, column=0, sticky = W, padx=10, pady=10)

        self.v = StringVar()
        self.E2 = Entry(master, bd =5,textvariable=self.v,width=50)
        self.E2.grid( row=1, column=1, padx=2, pady=10)


        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = master
        options['title'] = 'Select Location:'


        self.B1=Button(master, text='Browse', command=self.askdirectory,bd=2)
        self.B1.grid( row=1, column=2, padx=6, pady=0, sticky= E )

        self.L3 = Label(master, text="Available Clients")
        self.L3.grid( row=2, column=0, sticky = W, padx=10, pady=10)

        #sb = Scrollbar(win,orient=VERTICAL)

        self.lb1 = Listbox(master,height=5,width=50,selectmode=MULTIPLE)
        self.lb1.grid( row=2, column=1, sticky = W,columnspan = 1, padx=10, pady=10)
        #self.lb1.insert(1,"List of connections available")

        self.s = ttk.Scrollbar(master, orient=VERTICAL, command=(self.lb1).yview)
        self.s.grid(column=2, row=2, sticky=(W,N,S))
        self.lb1['yscrollcommand'] = self.s.set

        #sb.configure(command=lb1.yview)
        #lb1.configure(yscrollcommand=sb.set)

        self.L4 = Label(master, text="Connected Clients")
        self.L4.grid( row=4, column=0, sticky = W, padx=10, pady=10)

        self.B2=Button(master, text='Connect',command=self.start_pushed)
        self.B2.grid( row=3, column=1, padx=4, pady=10 )

        self.lb2 = Listbox(master,height=5,width=50,selectmode=MULTIPLE)
        self.lb2.grid( row=4, column=1, sticky = W,columnspan = 1, padx=10, pady=10)
        #self.lb2.insert(1,"List of accepted connections")

        self.s1 = ttk.Scrollbar(master, orient=VERTICAL, command=(self.lb2).yview)
        self.s1.grid(column=2, row=4, sticky=(W,N,S))
        self.lb2['yscrollcommand'] = self.s1.set


        

        self.B3=Button(master, text='Start Download',command=self.start_download)
        self.B3.grid( row=5, column=1, padx=4, pady=10 )

        self.progress = ttk.Progressbar(master, orient="horizontal", 
                                        length=200, mode="determinate")
        #self.progress.grid(row=6, column=1, padx=4, pady=10)

        self.bytes = 0
        self.maxbytes = 0
        self.master=master
        self.progress['value']=0
        self.progress["maximum"] = 55238




    def askdirectory(self):

        #Returns a selected directoryname.    
        #print (self.E1).get()
        (self.v).set(tkFileDialog.askdirectory(**self.dir_opt)) 
        
    def start_download(self):
        #print "here in start"
        global start_flag, should_proceed
        start_flag = True
        should_proceed=True
        #self.start()

    def start_pushed(self):

        if len(self.urlentered.get())!=0 and len(self.v.get())!=0:
            try:
                temp=urllib.urlopen(self.urlentered.get())
            except:
                #print e.code
                print "\n\n-----URL invalid------\n\n"
                tkMessageBox.showinfo("Error", "URL invalid")
            else:
                global connect_flag
                connect_flag = True
        else:
            print "\n\n-----URL and directory can't be empty------\n\n"
            tkMessageBox.showinfo("Error", "URL and directory can't be empty")
 

    def threader(self):
        self.thread2 = threading.Thread(target=self.start)
        self.thread2.start()


    def start(self):
        global server

        self.progress["value"] = 0
        self.maxbytes = server.clients_handler[0].sizeToDownload
        self.progress["maximum"] = server.clients_handler[0].sizeToDownload
        #self.read_bytes()


    def read_bytes(self,i):
        '''simulate reading 500 bytes; update progress bar'''
        #global server
        print "\n\n----here",i,"  ",server.clients_handler[i].downloadedTillNow,"---\n\n"
        self.bytes = server.clients_handler[i].downloadedTillNow
        self.progress["value"] = self.bytes
        if self.bytes < 55238:
            # read more bytes after 100 ms
            self.master.after(1000, self.read_bytes(i))
        #else:
        #   self.endCommand()

        # Add more GUI stuff here

    def processIncoming(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do what it says
                # As a test, we simply print it
                #print msg
            except Queue.Empty:
                pass

class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI. We spawn a new thread for the worker.
        """
        self.master = master

        # Create the queue
        self.queue = Queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.endApplication)

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = 1
        #self.thread1 = threading.Thread(target=self.workerThread1)
        #self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(100, self.periodicCall)

    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select()'.
        One important thing to remember is that the thread has to yield
        control.
        """
        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following 2 lines with the real
            # thing.
            sleep(2 * 0.3)
            msg = 2
            self.queue.put(msg)

    def endApplication(self):
        #print "hey"
        self.running = 0













"""def askdirectory():
    return v.set(tkFileDialog.askdirectory(**dir_opt))"""


 


count_conn = 0

def run_thread_gui(a) :
    global client
    client = ThreadedClient(win)
    
    win.mainloop()


def client_role_play(a):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))



    request_to_download=client_socket.recv(8812)
    print request_to_download
    print "1.Yes\n0.No"

    choice=raw_input()

    if choice=='1':
        response="acceptance=1"
    else:
        response="acceptance=0"

    client_socket.send(response)

    if choice=='1':
        client_no=int(client_socket.recv(8812))
    no_of_threads=2
    #client_no=1

    if choice=='1':

        url = client_socket.recv(8812)
        start_from=int(client_socket.recv(8812))
        packet_size_each_client=int(client_socket.recv(8812))

        print "\n\n------amount to download= ",packet_size_each_client,"--------\n\n"   
        
        packet_size_each_thread=[]
        i=0
        while i<no_of_threads:
            if i != no_of_threads-1:
                packet_size_each_thread.append(packet_size_each_client/no_of_threads)
            else:
                packet_size_each_thread.append((packet_size_each_client/no_of_threads) + (packet_size_each_client%no_of_threads))
            i+=1
        
        #print packet_size_each
        u = urllib2.urlopen(url)

        main_data=[]
        main_data.append([])
        main_data.append([])

        #suppose this is client 1




        def download(i):
            
            x=client_no*no_of_threads
            if i==x:
                start=start_from
            else:
                start=start_from + (i-(x))*packet_size_each_thread[i-(x)-1]
            start1=str(start)
            end=start+ packet_size_each_thread[i-(x)]-1
            end1=str(end)
            req = urllib2.Request(url, headers={'Range':'bytes='+start1+'-'+end1})
            u = urllib2.urlopen(req)
            block_sz = 8192
            file_size_dl = start
            temp='\0'
            while True:
                data=u.read(block_sz)
                if not data:
                    break
                print('%d Fetched %s from %s' % (i,len(data), url))
                temp=temp+data
                client_socket.send(str(len(data)))
                #f.seek(file_size_dl)
                #ile_size_dl += len(data)
                #f.write(data)
            
            main_data[i-x]=temp[1:]
            #sock.send(temp)
            #print len(temp)
            #f.seek(start)
            #f.write(temp)

            

        def start_parallel():
            #result = Queue.Queue()
            x=client_no*no_of_threads
            y=x+no_of_threads

            threads = [threading.Thread(target=download, args = (i,)) for i in range(x,y)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            




        st=time()
        start_parallel()
        print time()-st

        print "\n\n------sending data-----\n\n"
        client_socket.send("Sending data")
        for i in range(2):
            print len(main_data[i])
            client_socket.send(main_data[i])
        print "\n\n----completed-----\n\n"
        #time.sleep(2)
            
        '''data = client_socket.recv(512)
        if ( data == 'q' or data == 'Q'):
            client_socket.close()
            break;
        else:
            print "RECIEVED:" , data
            data = raw_input ( "SEND( TYPE q or Q to Quit):" )
            if (data <> 'Q' and data <> 'q'):
                client_socket.send(data)
            else:
                client_socket.send(data)
                client_socket.close()
                break;'''

    #to keep the cmd on
    while True:
        a=1




if __name__ == "__main__": # Start the server in a new thread
    #thread.start_new_thread(run_thread,("erte",) )
    thread.start_new_thread(client_role_play,("erte",) )
    thread.start_new_thread(run_thread_gui,("erte",) )
    



#to keep the cmd on
while True:
    a=1
   
