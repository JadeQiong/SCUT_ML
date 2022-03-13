def detect_face(self, img):
    ''' Detect face over image '''
    boxes_align = np.array([])
    landmark_align = np.array([])
    t = time.time()
    # pnet
    if self.pnet_detector:
        boxes, boxes_align = self.detect_pnet(img)
        if boxes_align is None:
            return np.array([]), np.array([])
        t1 = time.time() - t
        t = time.time()
    # rnet
    if self.rnet_detector:
        boxes, boxes_align = self.detect_rnet(img, boxes_align)
        if boxes_align is None:
            return np.array([]), np.array([])
        t2 = time.time() - t
        t = time.time()
    # onet
    if self.onet_detector:
        boxes_align, landmark_align = self.detect_onet(img, boxes_align)
        if boxes_align is None:
            return np.array([]), np.array([])
        t3 = time.time() - t
        t = time.time()
        print("time cost " + '{:.3f}'.format(t1 + t2 + t3) + '  pnet {:.3f}  rnet {:.3f}  onet {:.3f}'.format(t1, t2))
return boxes_align, landmark_align
