# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
from . import transforms as T


def build_transforms(cfg, is_train=True):
    
    if is_train:
        min_size = cfg.INPUT.MIN_SIZE_TRAIN
        max_size = cfg.INPUT.MAX_SIZE_TRAIN
        # flip_prob = 0.5  # cfg.INPUT.FLIP_PROB_TRAIN
        flip_prob = 0
        rotate_prob = 0.5
        pixel_aug_prob = 0.2
        random_crop_prob = cfg.DATASETS.RANDOM_CROP_PROB
    else:
        min_size = cfg.INPUT.MIN_SIZE_TEST
        max_size = cfg.INPUT.MAX_SIZE_TEST
        flip_prob = 0
        rotate_prob = 0
        pixel_aug_prob = 0
        random_crop_prob = 0

    to_bgr255 = cfg.INPUT.TO_BGR255
    normalize_transform = T.Normalize(
        mean=cfg.INPUT.PIXEL_MEAN, std=cfg.INPUT.PIXEL_STD, to_bgr255=to_bgr255
    )
    if cfg.DATASETS.AUG and is_train:
        transform = T.Compose(
            [
                T.RandomCrop(random_crop_prob),
                T.RandomBrightness(pixel_aug_prob),
                T.RandomContrast(pixel_aug_prob),
                T.RandomHue(pixel_aug_prob),
                T.RandomSaturation(pixel_aug_prob),
                T.RandomGamma(pixel_aug_prob),
                T.RandomRotate(rotate_prob),
                T.Resize(min_size, max_size),
                # T.RandomHorizontalFlip(flip_prob),
                T.ToTensor(),
                normalize_transform,
            ]
        )
    else:
        transform = T.Compose(
            [
                T.Resize(min_size, max_size),
                # T.RandomHorizontalFlip(flip_prob),
                T.ToTensor(),
                normalize_transform,
            ]
        )
    return transform
