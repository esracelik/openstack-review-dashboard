================================
Openstack Gerrit Review Searcher
================================

This simple project converts a filter text to a link address
that creates a dashboard in review.openstack.org page

Usage
=====

python -m reviewSearcher.main filter-file

Note that filter-file should be well organized, one can use
docfilter.txt or novafilter.txt for an example. White spaces 
and escape characters are significant

<a href="https://review.openstack.org/#/dashboard/?foreach=%28project%3Aopenstack%2Fnova+OR+project%3Aopenstack%2Fnova-specs+OR+project%3Aopenstack%2Fpython-novaclient+OR+project%3Aopenstack%2Fpuppet-nova+OR+project%3Aopenstack%2Fnova-powervm+OR+project%3Aopenstack%2Fnova-docker+OR+project%3Aopenstack%2Fnova-zvm-virt-driver+OR+project%3Aopenstack%2Fnova-solver-scheduler+OR+project%3Aopenstack%2Ffuel-plugin-nova-nfs+OR+project%3Aopenstack%2Fblazar-nova+OR+project%3Aopenstack%2Fec2-api%29+status%3Aopen+NOT+owner%3Aself+NOT+label%3AWorkflow%3C%3D-1+label%3AVerified%3E%3D1%252cjenkins+NOT+label%3ACode-Review%3C%3D-1%252cself+NOT+label%3ACode-Review%3E%3D1%252cself&title=Nova+Review+Inbox&You+are+a+reviewer+%28but+haven%27t+voted+in+the+current+revision%29=reviewer%3Aself&Needs+feedback+%28Changes+older+than+5+days+that+have+not+been+reviewed+by+anyone%29=NOT+label%3ACode-Review%3C%3D2+age%3A5d+limit%3A50&Needs+final+%2B2=label%3ACode-Review%3E%3D2+limit%3A50&Passed+Jenkins+%28with+no+negative+feedback%29=NOT+label%3ACode-Review%3E%3D2+NOT+label%3ACode-Review%3C%3D-1+limit%3A50&Wayward+Changes+%28Changes+with+no+code+review+in+the+last+two+days%29=NOT+label%3ACode-Review%3C%3D2+age%3A2d&All+Nova+Related=%28project%3Aopenstack%2Fnova+OR+project%3Aopenstack%2Fnova-specs+OR+project%3Aopenstack%2Fpython-novaclient+OR+project%3Aopenstack%2Fpuppet-nova+OR+project%3Aopenstack%2Fnova-powervm+OR+project%3Aopenstack%2Fnova-docker+OR+project%3Aopenstack%2Fnova-zvm-virt-driver+OR+project%3Aopenstack%2Fnova-solver-scheduler+OR+project%3Aopenstack%2Ffuel-plugin-nova-nfs+OR+project%3Aopenstack%2Fblazar-nova+OR+project%3Aopenstack%2Fec2-api%29+status%3Aopen">My Nova Dashboard</a>
