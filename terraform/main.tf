provider "google" {
  credentials = "${file("hitmebaby.json")}"
  project     = "eng-blade-242502"
  region      = "asia-southeast1"
  zone        = "asis-southeast1-b"
}
