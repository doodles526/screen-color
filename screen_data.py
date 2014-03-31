import gtk.gdk
import numpy
import time

while True:
	start = time.time()
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	
	#take the screenshot and convert to pixel buffer
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	#get a numpy array of elements
	b = pb.get_pixels_array()

	avg = numpy.mean(b, (0,1), dtype=numpy.int32)
	print str(avg[0]) + " " + str(avg[1]) + " " + str(avg[2])
