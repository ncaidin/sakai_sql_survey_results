# Sakai Tool Events
## Oracle
>SELECT 
  >count(se.event) num_events
>, se.event
> FROM 
  >sakai_event se
>WHERE se.event_date >= to_date('20120101 00:00','YYYYMMDD HH24:MI')
>AND se.event_date < to_date('20140101 00:00','YYYYMMDD HH24:MI')
>GROUP BY se.event
>ORDER BY num_events desc;
 
 
## MySQL
>SELECT
  >count(se.event) num_events
>, se.event
>FROM
  >SAKAI_EVENT se
>WHERE se.event_date >= str_to_date('20120101','%Y%m%d')
>AND se.event_date < str_to_date('20140101','%Y%m%d')
>GROUP BY se.event
>ORDER BY num_events desc;
### Sample Output
num_events  event
644 content.revise
583 realm.upd
348 content.new
318 content.available
317 pres.end
317 pres.begin
286 content.delete
285 realm.add
281 realm.del
175 site.upd
170 user.login
169 user.logout
153 profile.view.own
95  syllabus.read
94  server.start
92  org.theospi.template.revise
91  calendar.revise
89  search.query
44  profile.search.name
44  calendar.revise.event.frequency
43  calendar.revise.event.time
43  calendar.revise.event.type
43  calendar.new
43  calendar.revise.event.title
38  calendar.revise.event.exclusions
21  lessonbuilder.read
15  wiki.new
13  news.read
11  pageorder.reorder
11  profile.update
10  profile.info.update
9   lessonbuilder.create
8   site.add
8   calendar.delete.event
7   profile.friends.view.own
7   pageorder.disable
7   site.usersite.invalidate
7   annc.create
6   site.upd.site.mbrshp
6   profile.message.sent
6   calendar.create
6   profile.new
6   content.read
6   syllabus.post.new
5   profile.prefs.new
5   lessonbuilder.update
5   prefs.add
5   sitestats.admin.view
5   profile.privacy.new
5   user.site.membership.add
4   forums.response
4   memory.reset
4   user.add
3   news.revise
3   site.del
3   site.upd.grp.mbrshp
3   pageorder.hide
3   forums.reviseforum
3   forums.read
3   forums.new
2   pageorder.enable
2   asn.revise.title
2   asn.new.assignmentcontent
2   pageorder.show
2   profile.image.change.upload
2   asn.new.assignment
2   sitestats.view
2   syllabus.post.change
2   clog.post.created
1   forums.newforum
1   sam.assessment.create
--snip
 
# Sakai Tool Placements
## Both Oracle and MySQL
> SELECT
  >registration
>, count(distinct(t.site_id)) num_sites
>, count(distinct user_id) users_available_to
>FROM
  >SAKAI_SITE_TOOL t
>, SAKAI_SITE_USER u
>WHERE t.site_id NOT LIKE '~%'
>AND t.site_id NOT LIKE '!%'
>AND t.site_id = u.site_id
>GROUP BY registration
>ORDER BY users_available_to desc;
### Sample Output
+------------------------------+-----------+--------------------+
| registration                 | num_sites | users_available_to |
+------------------------------+-----------+--------------------+
| sakai.dropbox                |         2 |                  3 |
| sakai.iframe.site            |         6 |                  3 |
| sakai.messages               |         1 |                  3 |
| sakai.poll                   |         2 |                  3 |
| sakai.schedule               |         3 |                  3 |
| sakai.syllabus               |         1 |                  3 |
| sakai.announcements          |         5 |                  3 |
| sakai.forums                 |         2 |                  3 |
| sakai.lessonbuildertool      |         1 |                  3 |
| sakai.resources              |         6 |                  3 |
| sakai.synoptic.announcement  |         5 |                  3 |
| sakai.assignment.grades      |         4 |                  3 |
| sakai.gradebook.tool         |         2 |                  3 |
| sakai.news                   |         1 |                  3 |
| sakai.rwiki                  |         1 |                  3 |
| sakai.siteinfo               |         6 |                  3 |
| sakai.synoptic.chat          |         3 |                  3 |
| sakai.chat                   |         3 |                  3 |
| sakai.iframe                 |         1 |                  3 |
| sakai.mailtool               |         1 |                  3 |
| sakai.podcasts               |         1 |                  3 |
| sakai.samigo                 |         2 |                  3 |
| sakai.summary.calendar       |         2 |                  3 |
| sakai.synoptic.messagecenter |         2 |                  3 |
| osp.glossary                 |         1 |                  1 |
| osp.style                    |         1 |                  1 |
| osp.presentation             |         1 |                  1 |
| sakai.metaobj                |         1 |                  1 |
| sakai.sections               |         1 |                  1 |
| osp.presLayout               |         1 |                  1 |
| sakai.mailbox                |         2 |                  1 |
| osp.presTemplate             |         1 |                  1 |
+------------------------------+-----------+--------------------+

