import numpy as np
import matplotlib as plt
import atropy.io.fits. as fits

image_data = fits.open('C:\Users\sszz1\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)/UGC11411_F606W.fits')
image_data.info()
data = image_data[0].data
header = image_data[0].header

image = np.array(data)

max_value = np.percentile(image,99.8)
min_value = np.percentile(image,15)

plt.figure(figsize=(8,6))
plt.imshow(image, cmap='gray', vmax = max_value, vmin = min_value, origin = 'lower')
plt.xlim(1000,1750)
plt.ylim(300,1000)
plt.show()
specdata = fits.open('UGC11411_F606W.fits')
specdata.info()
spectrum = specdata[1].data
header = specdata[1].header
print(header)
flux = []
loglam = []

for i in range(len(spectrum)):
    flux.append(spectrum[i][0])
    loglam.append(spectrum[i][1])

flux = np.array(flux)
lam = 10**np.array(loglam)
plt.figure(figsize=(10,7))
plt.plot(lam,flux,c='black')
plt.title('Spectrum lines of NGC 5334', fontsize=20)
plt.xlabel('Wavelength (Angstroms)', fontsize=15)
plt.ylabel('Flux', fontsize=15)
plt.axvspan(5520,5650,facecolor='r', alpha=0.5)
