## App Service vs VM
App Service is suited when developer don't want full control over the application deployment and management whereas VM is suited when developer wants to take care of application deployment and management. So deployment will be faster in case of App Service.

Cost - 
For testing purposes, App Service provides a free tier but there is no such thing in VM. Also for a basic infrastructure App Service costs: ~$13.140/month and VM Costs $18.25/month

Scalability -
Both App Service and VM are scalable

Availability -
As per documentation, Both App Service and VM will be available more than 99.9% of the times


I have chosen App Service for deployiing my Application

In this project we just need the endpoint of hosted webapp and we need not focus of application deployment and management so I think App Service will be sufficient enough.


##In order to deploy on VM, we have to follow below steps - 
1. Launch a VM with required OS type
2. Install all the required dependencies
3. Configure the Networking and Firewall rules
4. Deploy the applicationthe app and any other needs would have to change for you to change your decision in the last section.* 