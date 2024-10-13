
import shortlist_applicants

job_description = """
Job Description:
We are seeking a motivated and detail-oriented IT Specialist to join our growing team. The ideal candidate will have at least 3 years of hands-on experience in managing IT infrastructure, troubleshooting network issues, and providing technical support to end users. As an IT Specialist, you will play a crucial role in ensuring the smooth operation of our IT systems and networks, offering timely solutions to technical problems, and enhancing the overall security and efficiency of our technological assets.

Key Responsibilities:
Provide technical support to employees across departments, resolving hardware, software, and network-related issues.
Install, configure, and maintain computer systems, servers, and network infrastructure.
Manage and maintain Windows and Linux servers, ensuring uptime and performance.
Monitor and troubleshoot network connectivity issues, including routers, switches, and firewalls.
Perform regular system updates, backups, and maintenance for data integrity and security.
Collaborate with the IT team to implement cybersecurity policies and monitor system vulnerabilities.
Manage Active Directory, including user account setup, permissions, and security protocols.
Provide support for cloud infrastructure (AWS, Azure, or Google Cloud) as needed.
Document IT procedures, system configurations, and troubleshooting guides.
Required Qualifications:
Bachelor’s Degree in Information Technology, Computer Science, or a related field.
A minimum of 3 years of experience as an IT Specialist, System Administrator, or in a similar role.
Strong knowledge of networking protocols, including TCP/IP, DNS, DHCP, VPN, and firewall configurations.
Experience with server administration (Windows and/or Linux).
Hands-on experience in troubleshooting hardware and software issues.
Proficiency in managing Active Directory and Office 365 environments.
Knowledge of cloud computing platforms like AWS, Azure, or Google Cloud.
Familiarity with IT security best practices and cybersecurity measures.
"""
passed_applicants = shortlist_applicants.shortlist_applicants(job_description)
print([i[1] for i in passed_applicants])