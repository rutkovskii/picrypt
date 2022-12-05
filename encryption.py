import PHE.Paillier as Paillier
import PHE.ImageCryptography as ImageCryptography
from PIL import Image

# generate keys
PublicKey,PrivateKey = Paillier.generate_keys(128)
print(PublicKey)


# image path
imgpath = "./assets/before.jpeg"
image1 = Image.open(imgpath)


cipherimg = ImageCryptography.ImgEncrypt(PublicKey, image1)

cipherimg.show()
