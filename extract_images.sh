function extract_images {
  ffmpeg -i "${@}" thumb%04d.jpg -hide_banner
}

extract_images
