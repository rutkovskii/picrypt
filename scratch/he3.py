import concrete.numpy as cnp
import cv2
import numpy as np

image1_path = "./assets/before.jpeg"
image2_path = "./assets/after.jpeg"

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)
result = cv2.subtract(image1, image2)

image1 = image1.astype(np.int64)
image2 = image2.astype(np.int64)

@cnp.compiler({"image1": "clear", "image2": "encrypted"})
def f(image1, image2):
    return (image1 - image2).clip(0, 255)

inputset = [(image1, image2)]  # you may want to add more samples to this, maybe random ones
circuit = f.compile(inputset, enable_unsafe_features=True, virtual=True)

homomorphic_result = circuit.encrypt_run_decrypt(image1, image2)
homomorphic_encrypted = circuit.encrypt(image1, image2)
image = homomorphic_result.astype(np.uint8)
cv2.imshow("Difference Image Normal", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(type(image))
assert np.array_equal(result, homomorphic_result)