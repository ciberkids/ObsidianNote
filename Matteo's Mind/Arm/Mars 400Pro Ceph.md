

https://www.ambedded.com.tw/en/product/ceph-storage-appliance.html

## Images

![[Pasted image 20240806132536.png]]
## Specs

##### Server Platform

|   |   |
|---|---|
|Processor|8x Arm server with Arm A72 64-bit Quad-Core Processors @ 1.2 GHz, Total 32 cores|
|Memory|4 GB DDR4 per microserver, Total 32GB|
|Network Interfaces|- Each Arm server has two 2.5 Gbps Ethernet<br>- Two in-chassis switches connect internally with 8 microservers<br>- Two 10Gb uplink Ethernet uplink ports on each in-chassis switch. Total 4x 10Gb for uplink.<br>- SPF+ & 10G base-T combo ports|
|Storage device &  <br>Interfaces|Every Arm Server has  <br>- 16GB eMMC for system and<br>- 120 GB M.2 SATA SSD for BlueStoreblue store use<br>- OSD disk: one SATA 6Gb 3.5” HDD or 2.5” SSD|
|System Management|One BMC to manage 8 micro-server in the chassis|
|Power Consumption|Normal: 70 Watts  <br>Maximum: 105 Watts|
|Power Supply|- 2x 300W redundant power supply, 80 PLUS Platinum<br>- AC input: 100-240Vac / 7-3A, 50-60Hz|
|Certificate of  <br>Conformity|- CE Mark<br>- FCC<br>- UKCA|
|Package include|- 1x Mars 400 Appliance<br>- 1x Mounting rail<br>- 2x 2 meters C13 to C14 power cords<br>- Optional Cable Management Arm|
|Mechanical|- Form factor 1U 19" rack mount<br>- Server dimensions: 440 x 42 x 746 mm<br>- Packaging dimensions: 930 x 580 x 215 mm<br>- Slide rail: Included|
|Support and  <br>Warranty|- 3 years software update and professional service<br>- 3 years hardware warranty<br>- Optional extended warranty and service|

  

##### Software

|   |   |
|---|---|
|Ceph Version|Ambedded tuned Ceph community versions|
|Management Interface|- Ambedded Web-based user interface: UniVirStor(UVS) Manager<br>- Command Line Interface|
|Automation|The UniVirStor Ceph management UI (UVS Manager) automate management functions for day-1 and day 2 operations, including cluster deployment, storage service provisioning, monitoring, and software updates.|
|Access  <br>Authentication  <br>Control|- Policy control to limit users to access pool & block device<br>- Ability to Integrate with Microsoft Active Directory, lightweight directory access protocol (LDAP), AWS Auth, and KeyStone|
|Multi-protocol  <br>support|A storage platform supports multiple industry-standard storage protocols for block, file and object storage.|
|Monitoring &  <br>Notification|- UVS, Ceph, and Grafana dashboard<br>- Alert sent through email<br>- SNMP|

  

##### Storage Pool

|   |   |
|---|---|
|Scale-out cluster|- Grow the cluster to thousands of storage drives<br>- No single point of failure<br>- Cluster performance is linearly scalable with the number of drives (OSD).|
|Self-healing and  <br>auto rebalancing|- Balances data distribution throughout the cluster nodes<br>- Handles failures without interruption, automatically recovering to the predefined data resilience|
|Highly available|Withstand loss of multiple nodes/racks without disrupting service availability or data safety.|
|Data protection|- Stripping, erasure coding, or replication across nodes with predefined rule<br>- Configurable number of replica and erasure coding profile<br>- CLAY erasure coding to reduce the data recovery time<br>- Renamable bucket type: root, region, zone, data center, room, PDU, raw, rack, chassis|
|Disk encryption|OSD disk drives can be encrypted to protect data when drives are removed|
|Data Compression|Inline object compression with target compression ratio|
|Cache Tiering|Support using a faster storage pool as cache tier of a capacity pool|

  

##### Deployment and Management

|   |   |
|---|---|
|Software update|- Automated rolling update without downtime. Data services are available during the update.<br>- Updates include Linux, Ceph, and UVS manager|
|General  <br>management|- Host management: Scan and management server nodes in the Ceph cluster<br>- Deploy the NTP server or use an external NTP server<br>- Push NTP client to ceph hosts<br>- Log management<br>- Notification<br>- User management|
|Ceph daemon  <br>services|- Cluster initialization<br>- Deploy and manage MON, OSD, MDS, RGW<br>- OSD encryption|

  

##### Storage Protocols  
RADOS Block Storage (RBD)

|   |   |
|---|---|
|RBD Image  <br>Management|- Image create, delete<br>- Select pool, name, image size, object size<br>- Image edit|
|Dynamic  <br>volume resizing|Ability to expand Ceph block devices with no downtime|
|RBD Mirroring  <br>for off-site  <br>active-standby  <br>backup|- Create mirroring service between multiple clusters or sites<br>- Select pool/image for mirroring<br>- Manage snapshot schedules<br>- Image promote/demote|
|RBD Snapshot|- Snapshots of individual block devices with no downtime or performance impact<br>- Create and manage snapshots of images to retain a history on an image’s state<br>- snapshot rollback|
|Copy on  <br>Write clone|Instant provisioning of tens or hundreds of virtual machine instances from the same image with zero wait time|
|Thing Provisions|Enable over-provisioning of storage and immediate VM or container instance launch.|
|iSCSI|- Deploy iSCSI gateway on hosts or VMs<br>- Create and manage LUN<br>- ACL: IQN and CHAP authentication<br>- Multi-Path IO support|

  

##### Shared File System (NAS)

|   |   |
|---|---|
|CephFS|- Deploy & manage Metadata servers (MDS)<br>- POSIX compatible file system: kernel and FUSE clients<br>- Multiple CephFS<br>- Support volumes, sub-volume and sub-volume groups|

  

##### Object Storage

|   |   |
|---|---|
|Object API|Amazon S3 and OpenStack Swift compatible APIs|
|RADOS  <br>gateway for  <br>Active-Active  <br>access|- Deploy RADOS multi-zone gateways<br>- Multi-site support for sync and access from multiple ceph clusters<br>- RGW User and key management<br>- RGW Pool management, auto-create RGW pools|
|Write Once  <br>Read Many  <br>(WORM)|S3 object lock with the read-only capability to store objects using a the WORM mode preventing objects from being deleted or overwritten|
|Encryption|Server-side encryption and client provided key encryption|

  

##### Cloud-Native and Virtualization

|   |   |
|---|---|
|Platforms|- Kubernetes container storage interface (CSI)<br>- OpenStack Cinder, Glance, and Nova, Manila, Swift API<br>- CloudStack libvirt<br>- Proxmox<br>- VMWare iSCSI, NFS<br>- Windows Ceph client driver|

  

##### Conventional file storage

|   |   |
|---|---|
|NFS, SMB  <br>FTP, HTTP|Use CephFS, S3 or block as the back store to export NFS, SMB, FTP, and HTTP through gateways|