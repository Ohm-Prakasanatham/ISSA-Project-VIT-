import marshal,base64
exec(base64.b64decode(" ZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAKaW1wb3J0IGNmc2NyYXBlCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IGRlcXVlCmltcG9ydCBqc29uCmltcG9ydCBubWFwCmltcG9ydCBvcwpmcm9tIG9zIGltcG9ydCBzeXN0ZW0KaW1wb3J0IHJlCmltcG9ydCByZXF1ZXN0cwppbXBvcnQgcmVxdWVzdHMuZXhjZXB0aW9ucwppbXBvcnQgcmVxdWVzdHMgYXMgcmVzCmZyb20gcmVxdWVzdHMgaW1wb3J0IGdldAppbXBvcnQgc3lzCmltcG9ydCB0aW1lCmZyb20gdGltZSBpbXBvcnQgZ210aW1lLCBzdHJmdGltZQpmcm9tIHVybGxpYi5lcnJvciBpbXBvcnQgVVJMRXJyb3IKZnJvbSB1cmxsaWIucGFyc2UgaW1wb3J0IHVybHNwbGl0CmltcG9ydCB1cmxsaWIzCmltcG9ydCB1cmxsaWIucmVxdWVzdApmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCB1cmxvcGVuCmltcG9ydCB1cmxsaWIucGFyc2UKaW1wb3J0IHdlYnRlY2gKCgpkZWYgYmFubmVyKCk6CiAgICBwcmludCgiIiIgXDAzM1sxOzM0bQrilojilojilojilojilojilojilZcgIOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilZcg4paI4paI4pWXICDilojilojilZcgICAg4paI4paI4pWXICAgIOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKVlyAK4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWRIOKWiOKWiOKVlOKVnSAgICDilojilojilZEgICAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWU4pWQ4pWQ4paI4paI4pWXCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4paI4paI4paI4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4pWU4pWdICAgICDilojilojilZEg4paI4pWXIOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWU4pWdCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4paI4paI4pWXICAgICDilojilojilZHilojilojilojilZfilojilojilZHilojilojilZTilZDilZDilZ0gIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlwrilojilojilojilojilojilojilZTilZ3ilojilojilZEgIOKWiOKWiOKVkeKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZcgICAg4pWa4paI4paI4paI4pWU4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4paI4paI4paI4paI4pWU4pWdCuKVmuKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZ0gIOKVmuKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ0gICAg4pWa4pWQ4pWQ4pWd4pWa4pWQ4pWQ4pWdIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVkOKVkOKVkOKVkOKVnSAgIFYxLjMKIFdFIEFSRSBBTk9OWU1PVVMgICAgIFdFIEFSRSBMRUdJT04gICAgICAgV0UgRE8gTk9UIEZPUkdJVkUKICAgICAgICAgICAgICAgICAgICAgICAgRVhQRUNUIFVTICAgICAgICAgICAgXDAzM1sxO20KICAgICAgICBcMDMzWzM0bURhcmsgV0VCOkluZm9ybWF0aW9uIEdhdGhlcmluZyBUb29sIFwwMzNbMG0KICAgICAgICBcMDMzWzM0bUF1dGhvciAgOiBBS0FTSCBCTEFDSyBIQVQgXDAzM1swbQogICAgICAgIFwwMzNbMzRtR2l0aHViICA6IGh0dHBzOi8vZ2l0aHViLmNvbS9ha2FzaGJsYWNraGF0IFwwMzNbMG0KICAgICAgICBcMDMzWzM0bVdoYXRzQXBwOiArOTEgODM4OTAyMDk0OSBcMDMzWzBtCiAgICAgICAgXDAzM1szNG1Zb3VUdWIgIDogVEVDSE5JQ0FMIEFLQVNIIFNLSUxMUyBcMDMzWzBtCiAgICAgICAgICAgICIiIikKZGVmIG1lbnUoKToKICAgIHByaW50KCJcblwwMzNbMTszNG1bK10gMS4gICBFdGhlckFwZSDigJMgR3JhcGhpY2FsIE5ldHdvcmsgTW9uaXRvciAocm9vdClcMDMzWzE7bSIpCiAgICBwcmludCgiXDAzM1sxOzM0bVsrXSAyLiAgIEROUyBMb29rdXBcMDMzWzE7bSIpCiAgICBwcmludCgiXDAzM1sxOzM0bVsrXSAzLiAgIFdob2lzIExvb2t1cCBcMDMzWzE7bSIpCiAgICBwcmludCgiXDAzM1sxOzM0bVsrXSA0LiAgIE5tYXAgUG9ydCBTY2FuXDAzM1sxO20iKQogICAgcHJpbnQoIlwwMzNbMTszNG1bK10gNS4gICBIVFRQIEhlYWRlciBHcmFiYmVyXDAzM1sxO20iKQogICAgcHJpbnQoIlwwMzNbMTszNG1bK10gNi4gICBDbGlja2phY2tpbmcgVGVzdCAtIFgtRnJhbWUtT3B0aW9ucyBIZWFkZXJcMDMzWzE7bSIpCiAgICBwcmludCgiXDAzM1sxOzM0bVsrXSA3LiAgIFJvYm90cy50eHQgU2Nhbm5lclwwMzNbMTttIikKICAgIHByaW50KCJcMDMzWzE7MzRtWytdIDguICAgQ2xvdWRmbGFyZSBDb29raWUgc2NyYXBlclwwMzNbMTttIikKICAgIHByaW50KCJcMDMzWzE7MzRtWytdIDkuICAgTGluayBHcmFiYmVyXDAzM1sxO20iKQogICAgcHJpbnQoIlwwMzNbMTszNG1bK10gMTAuICBJUCBMb2NhdGlvbiBGaW5kZXJcMDMzWzE7bSIpCiAgICBwcmludCgiXDAzM1sxOzM0bVsrXSAxMS4gIERldGVjdGluZyBDTVMgd2l0aCBJZGVudGlmaWVkIFRlY2hub2xvZ2llc1wwMzNbMTttIikKICAgIHByaW50KCJcMDMzWzE7MzRtWytdIDEyLiAgVHJhY2Vyb3V0ZVwwMzNbMTttIikKICAgIHByaW50KCJcMDMzWzE7MzRtWytdIDEzLiAgQ3Jhd2xlciB0YXJnZXQgdXJsICsgUm9ib3RzLnR4dFwwMzNbMTttIikKICAgIHByaW50KCJcMDMzWzE7MzRtWytdIDE0LiAgQ2VydGlmaWNhdGUgVHJhbnNwYXJlbmN5IGxvZyBtb25pdG9yXDAzM1sxO20iKQogICAgcHJpbnQoIlwwMzNbMTszNG1beF0gMTUuICBFeGl0XDAzM1sxO21cbiIpCgoKZGVmIGZ1bigpOgogICAgY2hvaWNlID0gKCIxIikKICAgIGJhbm5lcigpCgogICAgd2hpbGUgY2hvaWNlICE9ICgiMTIiKToKICAgICAgICBtZW51KCkKICAgICAgICBjaG9pY2UgPSBpbnB1dCgiXDAzM1sxOzM0bVsrXVwwMzNbMTttIFwwMzNbMTs5MW1FbnRlciB5b3VyIGNob2ljZTpcMDMzWzE7bSAiKQoKICAgICAgICBpZiBjaG9pY2UgPT0gKCIzIik6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHRhcmdldCA9IGlucHV0KCJcMDMzWzE7OTFtWytdIEVudGVyIERvbWFpbiBvciBJUCBBZGRyZXNzOiBcMDMzWzE7bSIpLmxvd2VyKCkKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICAgICAgcHJpbnQoIlwwMzNbMzRtW35dIFNlYXJjaGluZyBmb3IgV2hvaXMgTG9va3VwOiBcMDMzWzBtIi5mb3JtYXQodGFyZ2V0KSArIHRhcmdldCkKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMS41KQogICAgICAgICAgICAgICAgY29tbWFuZCA9ICgid2hvaXMgIiArIHRhcmdldCkKICAgICAgICAgICAgICAgIHByb2NlcyA9IG9zLnBvcGVuKGNvbW1hbmQpCiAgICAgICAgICAgICAgICByZXN1bHRzID0gc3RyKHByb2Nlcy5yZWFkKCkpCiAgICAgICAgICAgICAgICBwcmludChyZXN1bHRzICsgY29tbWFuZCkKCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgICAgICBwYXNzCgogICAgICAgIGVsaWYgY2hvaWNlID09ICgiMiIpOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICB0YXJnZXQgPSBpbnB1dCgiXDAzM1sxOzkxbVsrXSBFbnRlciBEb21haW4gb3IgSVAgQWRkcmVzczogXDAzM1sxO20iKS5sb3dlcigpCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oInJlc2V0IikKICAgICAgICAgICAgICAgIHByaW50KCJcMDMzWzM0bVt+XSBTZWFyY2hpbmcgZm9yIEROUyBMb29rdXA6IFwwMzNbMG0iLmZvcm1hdCh0YXJnZXQpICsgdGFyZ2V0KQogICAgICAgICAgICAgICAgdGltZS5zbGVlcCgxLjUpCiAgICAgICAgICAgICAgICBjb21tYW5kID0gKCJkaWcgIiArIHRhcmdldCArICIgK3RyYWNlIEFOWSIpCiAgICAgICAgICAgICAgICBwcm9jZXMgPSBvcy5wb3Blbihjb21tYW5kKQogICAgICAgICAgICAgICAgcmVzdWx0cyA9IHN0cihwcm9jZXMucmVhZCgpKQogICAgICAgICAgICAgICAgcHJpbnQocmVzdWx0cyArIGNvbW1hbmQpCgogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwoKICAgICAgICBlbGlmIGNob2ljZSA9PSAoIjEiKToKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJyZXNldCIpCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oImdub21lLXRlcm1pbmFsIC1lICdiYXNoIC1jIFwic3VkbyBldGhlcmFwZTsgZXhlYyBiYXNoXCInIikKCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgICAgICBwYXNzCgogICAgICAgIGVsaWYgY2hvaWNlID09ICgiNCIpOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICB0YXJnZXQgPSBpbnB1dCgiXDAzM1sxOzkxbVsrXSBFbnRlciBEb21haW4gb3IgSVAgQWRkcmVzczogXDAzM1sxO20iKS5sb3dlcigpCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oInJlc2V0IikKICAgICAgICAgICAgICAgIHByaW50KCJcMDMzWzM0bVt+XSBTY2FubmluZyBObWFwIFBvcnQgU2NhbjogXDAzM1swbSIgKyB0YXJnZXQpCiAgICAgICAgICAgICAgICBwcmludCgiVGhpcyB3aWxsIHRha2UgYSBtb21lbnQuLi4gR2V0IHNvbWUgY29mZmVlIPCfmIMgKVxuIikKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMS41KQoKICAgICAgICAgICAgICAgIHNjYW5uZXIgPSBubWFwLlBvcnRTY2FubmVyKCkKICAgICAgICAgICAgICAgIGNvbW1hbmQgPSAoIm5tYXAgLVBuICIgKyB0YXJnZXQpCiAgICAgICAgICAgICAgICBwcm9jZXNzID0gb3MucG9wZW4oY29tbWFuZCkKICAgICAgICAgICAgICAgIHJlc3VsdHMgPSBzdHIocHJvY2Vzcy5yZWFkKCkpCiAgICAgICAgICAgICAgICBsb2dQYXRoID0gImxvZ3Mvbm1hcC0iICsgc3RyZnRpbWUoIiVZLSVtLSVkXyVIOiVNOiVTIiwgZ210aW1lKCkpCgogICAgICAgICAgICAgICAgcHJpbnQocmVzdWx0cyArIGNvbW1hbmQgKyBsb2dQYXRoKQogICAgICAgICAgICAgICAgcHJpbnQoIlwwMzNbMzRtTm1hcCBWZXJzaW9uOiBcMDMzWzBtIiwgc2Nhbm5lci5ubWFwX3ZlcnNpb24oKSkKCiAgICAgICAgICAgIGV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoKICAgICAgICAgICAgICAgICAgICBwcmludCgiXG4iKQogICAgICAgICAgICAgICAgICAgIHByaW50KCJbLV0gVXNlciBJbnRlcnJ1cHRpb24gRGV0ZWN0ZWQuLiEiKQogICAgICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gKCI1Iik6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHRhcmdldCA9IGlucHV0KCJcMDMzWzE7OTFtWytdIEVudGVyIERvbWFpbiBvciBJUCBBZGRyZXNzOiBcMDMzWzE7bSIpLmxvd2VyKCkKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICAgICAgcHJpbnQoIlwwMzNbMzRtW35dIFNjYW5uaW5nIEhUVFAgSGVhZGVyIEdyYWJiZXI6IFwwMzNbMG1cbiIgKyB0YXJnZXQpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDEuNSkKICAgICAgICAgICAgICAgIGNvbW1hbmQgPSAoImh0dHAgLXYgIiArIHRhcmdldCkKICAgICAgICAgICAgICAgIHByb2NlcyA9IG9zLnBvcGVuKGNvbW1hbmQpCiAgICAgICAgICAgICAgICByZXN1bHRzID0gc3RyKHByb2Nlcy5yZWFkKCkpCiAgICAgICAgICAgICAgICBwcmludChyZXN1bHRzICsgY29tbWFuZCkKCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgICAgICBwYXNzCgogICAgICAgIGVsaWYgY2hvaWNlID09ICgiNiIpOgogICAgICAgICAgICB0YXJnZXQgPSBpbnB1dCgiXDAzM1sxOzkxbVsrXSBFbnRlciB0aGUgRG9tYWluIHRvIHRlc3Q6IFwwMzNbMTttIikubG93ZXIoKQogICAgICAgICAgICBvcy5zeXN0ZW0oInJlc2V0IikKCiAgICAgICAgICAgIGlmIG5vdCAodGFyZ2V0LnN0YXJ0c3dpdGgoImh0dHA6Ly8iKSBvciB0YXJnZXQuc3RhcnRzd2l0aCgiaHR0cHM6Ly8iKSk6CiAgICAgICAgICAgICAgICB0YXJnZXQgPSAiaHR0cDovLyIgKyB0YXJnZXQKICAgICAgICAgICAgcHJpbnQoIlwwMzNbMTszNG1bfl0gVGVzdGluZyBDbGlja2phY2tpbmcgVGVzdDogXDAzM1sxO20iICsgdGFyZ2V0KQogICAgICAgICAgICB0aW1lLnNsZWVwKDIpCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHJlc3AgPSByZXF1ZXN0cy5nZXQodGFyZ2V0KQogICAgICAgICAgICAgICAgaGVhZGVycyA9IHJlc3AuaGVhZGVycwogICAgICAgICAgICAgICAgcHJpbnQoIlxuSGVhZGVyIHNldCBhcmU6IFxuIikKICAgICAgICAgICAgICAgIGZvciBpdGVtLCB4ZnIgaW4gaGVhZGVycy5pdGVtcygpOgogICAgICAgICAgICAgICAgICAgIHByaW50KCJcMDMzWzE7MzRtIiArIGl0ZW0gKyAiOiIgKyB4ZnIgKyAiXDAzM1sxO20iKQoKICAgICAgICAgICAgICAgIGlmICJYLUZyYW1lLU9wdGlvbnMiIGluIGhlYWRlcnMua2V5cygpOgogICAgICAgICAgICAgICAgICAgIHByaW50KCJcblsrXSBcMDMzWzE7MzRtQ2xpY2sgSmFja2luZyBIZWFkZXIgaXMgcHJlc2VudFwwMzNbMTttIikKICAgICAgICAgICAgICAgICAgICBwcmludCgiWytdIFwwMzNbMTszNG1Zb3UgY2FuJ3QgY2xpY2tqYWNrIHRoaXMgc2l0ZSAhXDAzM1sxO21cbiIpCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIHByaW50KCJcblsqXSBcMDMzWzE7MzRtWC1GcmFtZS1PcHRpb25zLUhlYWRlciBpcyBtaXNzaW5nICEgXDAzM1sxO20iKQogICAgICAgICAgICAgICAgICAgIHByaW50KCJbIV0gXDAzM1sxOzM0bUNsaWNramFja2luZyBpcyBwb3NzaWJsZSx0aGlzIHNpdGUgaXMgdnVsbmVyYWJsZSB0byBDbGlja2phY2tpbmdcMDMzWzE7bVxuIikKCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXg6CiAgICAgICAgICAgICAgICBwcmludCgiXDAzM1sxOzM0bUV4Y2VwdGlvbiBjYXVnaHQ6ICIgKyBzdHIoZXgpKQoKICAgICAgICBlbGlmIGNob2ljZSA9PSAoIjciKToKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgdGFyZ2V0ID0gaW5wdXQoIlwwMzNbMTs5MW1bK10gRW50ZXIgRG9tYWluOiBcMDMzWzE7bSIpLmxvd2VyKCkKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICAgICAgcHJpbnQoIlwwMzNbMzRtW35dIFNjYW5uaW5nIFJvYm90cy50eHQgU2Nhbm5lcjogXDAzM1swbVxuIiArIHRhcmdldCkKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMS41KQoKICAgICAgICAgICAgICAgIGlmIG5vdCAodGFyZ2V0LnN0YXJ0c3dpdGgoImh0dHA6Ly8iKSBvciB0YXJnZXQuc3RhcnRzd2l0aCgiaHR0cHM6Ly8iKSk6CiAgICAgICAgICAgICAgICAgICAgdGFyZ2V0ID0gImh0dHA6Ly8iICsgdGFyZ2V0CiAgICAgICAgICAgICAgICByb2JvdCA9IHRhcmdldCArICIvcm9ib3RzLnR4dCIKCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgYm90cyA9IHVybG9wZW4ocm9ib3QpLnJlYWQoKS5kZWNvZGUoInV0Zi04IikKICAgICAgICAgICAgICAgICAgICBwcmludCgiXDAzM1szNG0iICsgKGJvdHMpICsgIlwwMzNbMTttIikKICAgICAgICAgICAgICAgIGV4Y2VwdCBVUkxFcnJvcjoKICAgICAgICAgICAgICAgICAgICBwcmludCgiXDAzM1sxOzMxbVstXSBDYW5cJ3QgYWNjZXNzIHRvIHtwYWdlfSFcMDMzWzE7bSIuZm9ybWF0KHBhZ2U9cm9ib3QpKQoKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBleDoKICAgICAgICAgICAgICAgIHByaW50KCJcMDMzWzE7MzRtRXhjZXB0aW9uIGNhdWdodDogIiArIHN0cihleCkpCgogICAgICAgIGVsaWYgY2hvaWNlID09ICgiOCIpOgogICAgICAgICAgICB0YXJnZXQgPSBpbnB1dCgiXDAzM1sxOzkxbVsrXSBFbnRlciBEb21haW46IFwwMzNbMTttIikubG93ZXIoKQogICAgICAgICAgICBpZiBub3QgKHRhcmdldC5zdGFydHN3aXRoKCJodHRwOi8vIikgb3IgdGFyZ2V0LnN0YXJ0c3dpdGgoImh0dHBzOi8vIikpOgogICAgICAgICAgICAgIAl0YXJnZXQgPSAiaHR0cDovLyIgKyB0YXJnZXQKICAgICAgICAgICAgb3Muc3lzdGVtKCJyZXNldCIpCiAgICAgICAgICAgIHByaW50KCJbK10gQ2xvdWRmbGFyZSBjb29raWUgc2NyYXBlciAiKQogICAgICAgICAgICB0aW1lLnNsZWVwKDEuNSkKCiAgICAgICAgICAgIHNlc3MgPSBjZnNjcmFwZS5jcmVhdGVfc2NyYXBlcigpCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgCXByaW50KCJbK10gVGFyZ2V0OiAiICsgdGFyZ2V0KQogICAgICAgICAgICAJcmVxdWVzdCA9ICJHRVQgLyBIVFRQLzEuMVxyXG4iCiAgICAgICAgICAgIAljb29raWVfdmFsdWUsIHVzZXJfYWdlbnQgPSBjZnNjcmFwZS5nZXRfY29va2llX3N0cmluZyh0YXJnZXQpCiAgICAgICAgICAgIAlyZXF1ZXN0ICs9ICJDb29raWU6ICVzXHJcblVzZXJfQWdlbnQ6ICVzXHJcbiIgJSAoY29va2llX3ZhbHVlLCB1c2VyX2FnZW50KQogICAgICAgICAgICAJZGF0YSA9IHNlc3MuZ2V0KHRhcmdldCkKICAgICAgICAgICAgCW91dCA9IEJlYXV0aWZ1bFNvdXAoZGF0YS5jb250ZW50LCdodG1sLnBhcnNlcicpCiAgICAgICAgICAgIAlwcmludCgiWytdIFByaW50IENvb2tpZVxuIikKICAgICAgICAgICAgCXByaW50KHJlcXVlc3QpCiAgICAgICAgICAgIAlvcy5zeXN0ZW0oJ3RwdXQgc2V0YWYgMTAnKQogICAgICAgICAgICAJcHJpbnQoIlxuWytdIFNjcmFwZXIgIikKICAgICAgICAgICAgCXByaW50KG91dCkKCiAgICAgICAgICAgIGV4Y2VwdCBWYWx1ZUVycm9yOgogICAgICAgICAgICAJcHJpbnQoJ1tYXSBVbmFibGUgdG8gZmluZCBDbG91ZGZsYXJlIGNvb2tpZXMuIFRoaXMgd2Vic2l0ZSBkb2VzIG5vdCBoYXZlIENsb3VkZmxhcmUgSVVBTSBlbmFibGVkLicpCgogICAgICAgIGVsaWYgY2hvaWNlID09ICgiOSIpOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICB0YXJnZXQgPSBpbnB1dCgiXDAzM1sxOzkxbVsrXSBFbnRlciBEb21haW46IFwwMzNbMTttIikubG93ZXIoKQogICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJyZXNldCIpCiAgICAgICAgICAgICAgICBwcmludCgiXDAzM1szNG1bfl0gU2Nhbm5pbmcgTGluayBHcmFiYmVyOiBcMDMzWzBtXG4iICsgdGFyZ2V0KQogICAgICAgICAgICAgICAgdGltZS5zbGVlcCgyKQogICAgICAgICAgICAgICAgaWYgbm90ICh0YXJnZXQuc3RhcnRzd2l0aCgiaHR0cDovLyIpIG9yIHRhcmdldC5zdGFydHN3aXRoKCJodHRwczovLyIpKToKICAgICAgICAgICAgICAgICAgICB0YXJnZXQgPSAiaHR0cDovLyIgKyB0YXJnZXQKICAgICAgICAgICAgICAgIGRlcSA9IGRlcXVlKFt0YXJnZXRdKQogICAgICAgICAgICAgICAgcHJvID0gc2V0KCkKCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgd2hpbGUgbGVuKGRlcSk6CiAgICAgICAgICAgICAgICAgICAgICAgIHVybCA9IGRlcS5wb3BsZWZ0KCkKICAgICAgICAgICAgICAgICAgICAgICAgcHJvLmFkZCh1cmwpCiAgICAgICAgICAgICAgICAgICAgICAgIHBhcnRzID0gdXJsc3BsaXQodXJsKQogICAgICAgICAgICAgICAgICAgICAgICBiYXNlID0gInswLnNjaGVtZX06Ly97MC5uZXRsb2N9Ii5mb3JtYXQocGFydHMpCgogICAgICAgICAgICAgICAgICAgICAgICBwcmludCgiWytdIENyYXdsaW5nIFVSTCAiICsgIlwwMzNbMzRtIiArIHVybCArICJcMDMzWzBtIikKICAgICAgICAgICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5nZXQodXJsKQogICAgICAgICAgICAgICAgICAgICAgICBleGNlcHQgKHJlcXVlc3RzLmV4Y2VwdGlvbnMuTWlzc2luZ1NjaGVtYSwgcmVxdWVzdHMuZXhjZXB0aW9ucy5Db25uZWN0aW9uRXJyb3IpOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgICAgICAgICAgICAgICAgIHNvdXAgPSBCZWF1dGlmdWxTb3VwKHJlc3BvbnNlLnRleHQsICJseG1sIikKICAgICAgICAgICAgICAgICAgICAgICAgZm9yIGFuY2hvciBpbiBzb3VwLmZpbmRfYWxsKCJhIik6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsaW5rID0gYW5jaG9yLmF0dHJzWyJocmVmIl0gaWYgImhyZWYiIGluIGFuY2hvci5hdHRycyBlbHNlICcnCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZiBsaW5rLnN0YXJ0c3dpdGgoIi8iKToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsaW5rID0gYmFzZSArIGxpbmsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIG5vdCBsaW5rIGluIGRlcSBhbmQgbm90IGxpbmsgaW4gcHJvOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRlcS5hcHBlbmQobGluaykKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlCgogICAgICAgICAgICAgICAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0OgogICAgICAgICAgICAgICAgICAgICAgICBwcmludCgiXG4iKQogICAgICAgICAgICAgICAgICAgICAgICBwcmludCgiWy1dIFVzZXIgSW50ZXJydXB0aW9uIERldGVjdGVkLi4hIikKICAgICAgICAgICAgICAgICAgICAgICAgdGltZS5zbGVlcCgxKQogICAgICAgICAgICAgICAgICAgICAgICBwcmludCgiXG4gXHRcMDMzWzM0bVshXSBJIGxpa2UgdG8gU2VlIFlhLCBIYWNraW5nIEFueXdoZXJlIC4uIVwwMzNbMG1cbiIpCgogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwoKICAgICAgICBlbGlmIGNob2ljZSA9PSAoIjEwIik6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHRhcmdldCA9IGlucHV0KCJcMDMzWzE7OTFtWytdIEVudGVyIERvbWFpbiBvciBJUCBBZGRyZXNzOiBcMDMzWzE7bSIpLmxvd2VyKCkKICAgICAgICAgICAgICAgIHVybCA9ICgiaHR0cDovL2lwLWFwaS5jb20vanNvbi8iKQogICAgICAgICAgICAgICAgcmVzcG9uc2UgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKHVybCArIHRhcmdldCkKICAgICAgICAgICAgICAgIGRhdGEgPSByZXNwb25zZS5yZWFkKCkKICAgICAgICAgICAgICAgIGpzbyA9IGpzb24ubG9hZHMoZGF0YSkKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICAgICAgcHJpbnQoIlwwMzNbMzRtW35dIFNlYXJjaGluZyBJUCBMb2NhdGlvbiBGaW5kZXI6IFwwMzNbMG0iLmZvcm1hdCh1cmwpICsgdGFyZ2V0KQogICAgICAgICAgICAgICAgdGltZS5zbGVlcCgxLjUpCgogICAgICAgICAgICAgICAgcHJpbnQoIlxuIFsrXSBcMDMzWzM0bVVybDogIiArIHRhcmdldCArICJcMDMzWzBtIikKICAgICAgICAgICAgICAgIHByaW50KCIgWytdICIgKyAiXDAzM1szNG0iICsgIklQOiAiICsganNvWyJxdWVyeSJdICsgIlwwMzNbMG0iKQogICAgICAgICAgICAgICAgcHJpbnQoIiBbK10gIiArICJcMDMzWzM0bSIgKyAiU3RhdHVzOiAiICsganNvWyJzdGF0dXMiXSArICJcMDMzWzBtIikKICAgICAgICAgICAgICAgIHByaW50KCIgWytdICIgKyAiXDAzM1szNG0iICsgIlJlZ2lvbjogIiArIGpzb1sicmVnaW9uTmFtZSJdICsgIlwwMzNbMG0iKQogICAgICAgICAgICAgICAgcHJpbnQoIiBbK10gIiArICJcMDMzWzM0bSIgKyAiQ291bnRyeTogIiArIGpzb1siY291bnRyeSJdICsgIlwwMzNbMG0iKQogICAgICAgICAgICAgICAgcHJpbnQoIiBbK10gIiArICJcMDMzWzM0bSIgKyAiQ2l0eTogIiArIGpzb1siY2l0eSJdICsgIlwwMzNbMG0iKQogICAgICAgICAgICAgICAgcHJpbnQoIiBbK10gIiArICJcMDMzWzM0bSIgKyAiSVNQOiAiICsganNvWyJpc3AiXSArICJcMDMzWzBtIikKICAgICAgICAgICAgICAgIHByaW50KCIgWytdICIgKyAiXDAzM1szNG0iICsgIkxhdCAmIExvbjogIiArIHN0cihqc29bJ2xhdCddKSArICIgJiAiICsgc3RyKGpzb1snbG9uJ10pICsgIlwwMzNbMG0iKQogICAgICAgICAgICAgICAgcHJpbnQoIiBbK10gIiArICJcMDMzWzM0bSIgKyAiWmlwY29kZTogIiArIGpzb1siemlwIl0gKyAiXDAzM1swbSIpCiAgICAgICAgICAgICAgICBwcmludCgiIFsrXSAiICsgIlwwMzNbMzRtIiArICJUaW1lWm9uZTogIiArIGpzb1sidGltZXpvbmUiXSArICJcMDMzWzBtIikKICAgICAgICAgICAgICAgIHByaW50KCIgWytdICIgKyAiXDAzM1szNG0iICsgIkFTOiAiICsganNvWyJhcyJdICsgIlwwMzNbMG0iICsgIlxuIikKCiAgICAgICAgICAgIGV4Y2VwdCBVUkxFcnJvcjoKICAgICAgICAgICAgICAgIHByaW50KCJcMDMzWzE7MzFtWy1dIFBsZWFzZSBwcm92aWRlIGEgdmFsaWQgSVAgYWRkcmVzcyFcMDMzWzE7bSIpCgogICAgICAgIGVsaWYgY2hvaWNlID09ICgiMTEiKToKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgdGFyZ2V0ID0gaW5wdXQoIlwwMzNbMTs5MW1bK10gRW50ZXIgRG9tYWluOiBcMDMzWzE7bSIpLmxvd2VyKCkKICAgICAgICAgICAgICAgIGlmIG5vdCAodGFyZ2V0LnN0YXJ0c3dpdGgoImh0dHA6Ly8iKSBvciB0YXJnZXQuc3RhcnRzd2l0aCgiaHR0cHM6Ly8iKSk6CiAgICAgICAgICAgICAgICAgCXRhcmdldCA9ICJodHRwczovLyIgKyB0YXJnZXQKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICAgICAgcHJpbnQoIlwwMzNbMzRtW35dIERldGVjdGluZyBDTVMgd2l0aCBJZGVudGlmaWVkIFRlY2hub2xvZ2llcyBhbmQgQ3VzdG9tIEhlYWRlcnMgZnJvbSB0YXJnZXQgdXJsOiBcMDMzWzBtIikKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoNSkKICAgICAgICAgICAgICAgIGNvbW1hbmQgPSAoIm10ciAiICsgIi00IC1yd2MgMSAiICsgdGFyZ2V0KQogICAgICAgICAgICAgICAgb2JqID0gd2VidGVjaC5XZWJUZWNoKCkKICAgICAgICAgICAgICAgIHJlc3VsdHMgPSBvYmouc3RhcnRfZnJvbV91cmwodGFyZ2V0LCB0aW1lb3V0PTEpCiAgICAgICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKHJlc3VsdHMpCgogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwoKICAgICAgICBlbGlmIGNob2ljZSA9PSAoIjEyIik6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHRhcmdldCA9IGlucHV0KCJcMDMzWzE7OTFtWytdIEVudGVyIERvbWFpbiBvciBJUCBBZGRyZXNzOiBcMDMzWzE7bSIpLmxvd2VyKCkKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICAgICAgcHJpbnQoIlwwMzNbMzRtW35dIFNlYXJjaGluZyBmb3IgVHJhY2Vyb3V0ZSBcMDMzWzBtIi5mb3JtYXQodGFyZ2V0KSArIHRhcmdldCkKICAgICAgICAgICAgICAgIHByaW50KCI+PiBUaGlzIHdpbGwgdGFrZSBhIG1vbWVudC4uLiBHZXQgc29tZSBjb2ZmZWUgPDwgKVxuIikKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoNSkKICAgICAgICAgICAgICAgIGNvbW1hbmQgPSAoIm10ciAiICsgIi00IC1yd2MgMSAiICsgdGFyZ2V0KQogICAgICAgICAgICAgICAgcHJvY2VzID0gb3MucG9wZW4oY29tbWFuZCkKICAgICAgICAgICAgICAgIHJlc3VsdHMgPSBzdHIocHJvY2VzLnJlYWQoKSkKICAgICAgICAgICAgICAgIHByaW50KCJcMDMzWzE7MzRtIiArIHJlc3VsdHMgKyBjb21tYW5kICsgIlwwMzNbMTttIikKICAgICAgICAgICAgICAgIGZ1bigpCgogICAgICAgICAgICBleGNlcHQgS2V5RXJyb3I6CiAgICAgICAgICAgICAJcGFzcwoKICAgICAgICBlbGlmIGNob2ljZSA9PSAoIjEzIik6CiAgICAgICAgICAgIHRhcmdldCA9IGlucHV0KCJcMDMzWzE7OTFtWytdIEVudGVyIERvbWFpbjogXDAzM1sxO20iKS5sb3dlcigpCiAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICBwcmludCgiXDAzM1szNG1bfl0gU3RhcnQgY3Jhd2xlci4uLiBcMDMzWzBtIikKICAgICAgICAgICAgdGltZS5zbGVlcCg1KQogICAgICAgICAgICBwcmludCgiWytdIFRhcmdldDogIiArIHRhcmdldCkKICAgICAgICAgICAgaWYgbm90ICh0YXJnZXQuc3RhcnRzd2l0aCgiaHR0cDovLyIpIG9yIHRhcmdldC5zdGFydHN3aXRoKCJodHRwczovLyIpKToKICAgICAgICAgICAgCXRhcmdldCA9ICJodHRwOi8vIiArIHRhcmdldAogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgIAljb250ZW50ID0gZ2V0KHRhcmdldCkudGV4dAogICAgICAgICAgICAJcmVnZXhfdCA9IHJlLmNvbXBpbGUociI8dGl0bGU+KC4qPyk8XC90aXRsZT4iKQogICAgICAgICAgICAJdGl0ID0gcmUuZmluZGFsbChyZWdleF90LCBjb250ZW50KQoKICAgICAgICAgICAgCXJlZ2V4X2wgPSByZS5jb21waWxlKHIiaHR0cFtzXT86Ly8oPzpbYS16QS1aXXxbMC05XXxbJC1fQC4mK118WyEqXChcKSxdfCg/OiVbMC05YS1mQS1GXVswLTlhLWZBLUZdKSkrIikKICAgICAgICAgICAgCWxpbmsgPSByZS5maW5kYWxsKHJlZ2V4X2wsIGNvbnRlbnQpCgogICAgICAgICAgICAJcm9ib3RzID0gZ2V0KHRhcmdldCArICIvcm9ib3RzLnR4dCIpLnRleHQKCiAgICAgICAgICAgIAlwcmludCgiWytdIFRpdGxlOiAiKyAnJy5qb2luKHRpdCkgKyAiXG4iKQogICAgICAgICAgICAJcHJpbnQoIlsrXSBFeHRyYWN0IGxpbmtzOiBcbiIgKyAnXG4nLmpvaW4obGluaykgKyAiXG4iKQogICAgICAgICAgICAJcHJpbnQoIlsrXSBSb2JvdHMudHh0OiBcbiIgKyByb2JvdHMpCgogICAgICAgICAgICBleGNlcHQgS2V5RXJyb3I6CiAgICAgICAgICAgICAJcGFzcwoKICAgICAgICBlbGlmIGNob2ljZSA9PSAoIjE0Iik6CiAgICAgICAgICAgIHRhcmdldCA9IGlucHV0KCJcMDMzWzE7OTFtWytdIEVudGVyIERvbWFpbjogXDAzM1swbSIpCiAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICBwcmludCgiXDAzM1szNG1bfl0gU2Nhbm5pbmcgQ2VydGlmaWNhdGUgVHJhbnNwYXJlbmN5IGxvZyBtb25pdG9yOiBcMDMzWzBtXG4iICsgdGFyZ2V0KQogICAgICAgICAgICB0aW1lLnNsZWVwKDEuNSkKICAgICAgICAgICAgcHJpbnQoIlsrXSBUYXJnZXQ6ICIgKyB0YXJnZXQpCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgCWhlYWRlcnMgPSB7CiAgICAgICAgICAgIAknVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xM18yKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjIuMC4zMjAyLjk0IFNhZmFyaS81MzcuMzYnLCB9CiAgICAgICAgICAgIAlyZXN1bHRzID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2FwaS5jZXJ0c3BvdHRlci5jb20vdjEvaXNzdWFuY2VzP2RvbWFpbj0nK3RhcmdldCsnJmV4cGFuZD1kbnNfbmFtZXMmZXhwYW5kPWlzc3VlciZleHBhbmQ9Y2VydCB8IGpxICIuW10uZG5zX25hbWVzW10iIHwgc2VkICJzL1wiLy9nIiB8IHNlZCAicy9cKlwuLy9nIiB8IHNvcnQgLXUgfCBncmVwICcrdGFyZ2V0LGhlYWRlcnM9aGVhZGVycykKICAgICAgICAgICAgCXJlc3VsdHMgPSByZXN1bHRzLnRleHQuc3BsaXQoJ1xuJykKICAgICAgICAgICAgCXByaW50KCpyZXN1bHRzLCBzZXAgPSAiXG4iKQoKICAgICAgICAgICAgZXhjZXB0IEtleUVycm9yOgogICAgICAgICAgICAgCXBhc3MKCiAgICAgICAgZWxpZiBjaG9pY2UgPT0gKCIxNSIpOgogICAgICAgICAgICB0aW1lLnNsZWVwKDEpCiAgICAgICAgICAgIHByaW50KCJcblx0XDAzM1szNG1CbHVlIEV5ZVwwMzNbMG0gRE9ORS4uLiBFeGl0aW5nLi4uIFwwMzNbMzRtTGlrZSB0byBTZWUgWWEgSGFja2luZyBBbnl3aGVyZSAuLiFcMDMzWzBtXG4iKQogICAgICAgICAgICBzeXMuZXhpdCgpCgogICAgICAgIGVsc2U6CiAgICAgICAgICAgIG9zLnN5c3RlbSgicmVzZXQiKQogICAgICAgICAgICBwcmludCgiXDAzM1sxOzMxbVstXSBJbnZhbGlkIG9wdGlvbi4uISBcMDMzWzE7bSIpCgoKIyA9PT09PSMgTWFpbiAjPT09PT0gIwoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIGZ1bigp "))
