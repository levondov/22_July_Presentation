import os, time

def pdf2svg(fname):
	fname_newpdf = fname[0:-4]+'c'+fname[len(fname)-4:]
	fnc_call = 'pdfcrop -m \'0 0 0 0\' ' + fname + ' ' + fname_newpdf
	print '++++++++++++ cropping pdf'
	os.system(fnc_call)
	
	time.sleep(1)
	
	fname_newsvg = fname_newpdf[0:-3] + 'svg'
	fnc_call2 = 'pdf2svg ' + fname_newpdf + ' ' + fname_newsvg
	print '++++++++++++ converting to svg'
	os.system(fnc_call2)
	
	time.sleep(1)
	
	fnc_call3 = 'rm ' + fname
	os.system(fnc_call3)
	  
pdf2svg('tune_range_1.pdf');	  
pdf2svg('tune_range_2.pdf');
pdf2svg('tune_range_TBT1.pdf');
pdf2svg('tune_range_TBT2.pdf');
