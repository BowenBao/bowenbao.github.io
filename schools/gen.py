﻿num = input('input number:')

str = """                        <!-- Tabs with icons on Card -->
                        <div class="card card-nav-tabs">
                            <div class="header header-success">
                                <!-- colors: "header-primary", "header-info", "header-success", "header-warning", "header-danger" -->
                                <div class="nav-tabs-navigation">
                                    <div class="nav-tabs-wrapper">
                                        <ul class="nav nav-tabs" data-tabs="tabs" id="card_tabs{0}">
                                            <li id="profile_tab{0}" class="active">
                                                <a href="#profile{0}" data-toggle="tab">
                                                    <i class="material-icons">business</i>
                                                    项目名称
                                                </a>
                                            </li>
                                            <li id="links_tab{0}">
                                                <a href="#links{0}" data-toggle="tab">
                                                    <i class="material-icons">cloud</i>
                                                    链接地址
                                                </a>
                                            </li>
                                            <li id="toefl_tab{0}">
                                                <a href="#toefl{0}" data-toggle="tab">
                                                    <i class="material-icons">translate</i>
                                                    TOEFL要求
                                                </a>

                                            </li>
                                            <li id="gre_tab{0}">
                                                <a href="#gre{0}" data-toggle="tab">
                                                    <i class="material-icons">assignment</i>
                                                    GRE要求
                                                </a>

                                            </li>
                                            <li id="recommend_tab{0}">
                                                <a href="#recommend{0}" data-toggle="tab">
                                                    <i class="material-icons">description</i>
                                                    推荐信要求
                                                </a>

                                            </li>
                                            <li id="bachelar_tab{0}">
                                                <a href="#bachelar{0}" data-toggle="tab">
                                                    <i class="material-icons">book</i>
                                                    本科学位要求
                                                </a>

                                            </li>
                                            <li id="gpa_tab{0}">
                                                <a href="#gpa{0}" data-toggle="tab">
                                                    <i class="material-icons">assessment</i>
                                                    GPA要求
                                                </a>

                                            </li>
                                            <li id="due_tab{0}">
                                                <a href="#due{0}" data-toggle="tab">
                                                    <i class="material-icons">schedule</i>
                                                    截止日期
                                                </a>

                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="content">
                                <div class="tab-content text-center">
                                    <div class="tab-pane active" id="profile{0}">
                                        <table class="table">
                                            <thead>
                                                <tr>
                                                    <th>信息</th>
                                                    <th>简介</th>
                                                    <th class="text-center">详细信息</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-left">项目名称</td>
                                                    <td class="text-left">MS CS</td>
                                                    <td class="td_actions">
                                                        <a href="#profile{0}" data-toggle="modal" data-target="#myModal{0}">
                                                            <i class="material-icons">business</i>
                                                            项目信息
                                                        </a>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="text-left">TOEFL要求</td>
                                                    <td class="text-left">86</td>
                                                    <td class="td_actions">
                                                        <a href="#toefl{0}" data-toggle="tab" onclick="
                                                                                                        $('#card_tabs{0}  li').removeClass('active');
                                                                                                        var maptab = document.getElementById('toefl_tab{0}');
                                                                                                        maptab.className = maptab.className + ' active';
                                                                                                        ">
                                                            <i class="material-icons">translate</i>
                                                            TOEFL要求
                                                        </a>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="text-left">GRE要求</td>
                                                    <td class="text-left">Required.</td>
                                                    <td class="td_actions">
                                                        <a href="#gre{0}" data-toggle="tab" onclick="
                                                                                                      $('#card_tabs{0}  li').removeClass('active');
                                                                                                      var maptab = document.getElementById('gre_tab{0}');
                                                                                                      maptab.className = maptab.className + ' active';
                                                                                                      ">
                                                            <i class="material-icons">assignment</i>
                                                            GRE要求
                                                        </a>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="text-left">推荐信要求</td>
                                                    <td class="text-left">3封</td>
                                                    <td class="td_actions">
                                                        <a href="#recommend{0}" data-toggle="tab" onclick="
                                                                                                            $('#card_tabs{0}  li').removeClass('active');
                                                                                                            var maptab = document.getElementById('recommend_tab{0}');
                                                                                                            maptab.className = maptab.className + ' active';
                                                                                                            ">
                                                            <i class="material-icons">description</i>
                                                            推荐信息
                                                        </a>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="text-left">本科学位要求</td>
                                                    <td class="text-left">full admit with prerequisite course work</td>
                                                    <td class="td_actions">
                                                        <a href="#bachelar{0}" data-toggle="tab" onclick="
                                                                                                           $('#card_tabs{0}  li').removeClass('active');
                                                                                                           var maptab = document.getElementById('bachelar_tab{0}');
                                                                                                           maptab.className = maptab.className + ' active';
                                                                                                           ">
                                                            <i class="material-icons">book</i>
                                                            本科学位
                                                        </a>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="text-left">GPA要求</td>
                                                    <td class="text-left">3.0 (需要成绩认证)</td>
                                                    <td class="td_actions">
                                                        <a href="#gpa{0}" data-toggle="tab" onclick="
                                                                                                      $('#card_tabs{0}  li').removeClass('active');
                                                                                                      var maptab = document.getElementById('gpa_tab{0}');
                                                                                                      maptab.className = maptab.className + ' active';
                                                                                                      ">
                                                            <i class="material-icons">assessment</i>
                                                            GPA要求
                                                        </a>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="text-left">截止日期</td>
                                                    <td class="text-left">
                                                        <strong>Fall</strong>, April 15; <strong>Winter</strong>, October 1; <strong>Spring</strong>, February 1.
                                                    </td>
                                                    <td class="td_actions">
                                                        <a href="#due{0}" data-toggle="tab" onclick="
                                              $('#card_tabs{0}  li').removeClass('active');
                                              var maptab = document.getElementById('due_tab{0}');
                                              maptab.className = maptab.className + ' active';
                                              ">
                                                            <i class="material-icons">schedule</i>
                                                            截止日期
                                                        </a>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                    <div class="tab-pane" id="links{0}">
                                        <button class="btn btn-simple btn-info" onclick="location.href='http://catalog.wwu.edu/preview_program.php?catoid=12&poid=5461&returnto=2524';">CS program</button>
                                        <button class="btn btn-simple btn-info" onclick="location.href='http://catalog.wwu.edu/content.php?catoid=12&navoid=2530';">admission</button>
                                    </div>
                                    <div class="tab-pane" id="toefl{0}">
                                        <div class="panel-body text-left">
                                            All applicants must demonstrate competence in written and spoken English. This can be done by submitting a satisfactory score on the international TOEFL or IELTS, taken within one year of the date of application. Minimum TOEFL score of 567 for the paper-based test; 227 for the computer-based test; 86 for the Internet-based test. IELTS minimum score is 7.0. Official test scores must be on file in the Graduate School prior to receipt of the application.
                                        </div>
                                    </div>
                                    <div class="tab-pane" id="gre{0}">
                                        <div class="panel-body text-left">
                                            GRE General Test. An applicant with an advanced degree need not submit test scores. A statement of purpose is recommended.
                                        </div>
                                    </div>
                                    <div class="tab-pane" id="recommend{0}">
                                        <div class="panel-body text-left">
                                            Three current letters of reference from professors in the applicant's undergraduate major field, or from professors of post-baccalaureate courses, or from others able to make an appropriate assessment of the applicant's academic or professional competence. The MBA and MPAcc programs require a résumé in lieu of references. The Educational Administration program requires a professional recommendation.
                                        </div>
                                    </div>
                                    <div class="tab-pane" id="bachelar{0}">
                                        <div class="panel-body text-left">
                                            <p>
                                                Students who have completed an undergraduate degree and who meet the requirements of the Graduate School and who show evidence of superior scholarship are invited to apply for admission to the graduate program in computer science. Students may be admitted into the computer science master's degree program in one of three ways: full admit, full admit with prerequisite course work, and provisional admit. Students who have a sufficient background in computer science, i.e. an undergraduate degree in Computer Science, and who meet the general requirements of the Graduate School can be given a "full admit." Due to the nature of this field of study, it is often the case that students with an undergraduate degree in an area other than computer science seek admission to the graduate program in computer science. Such students usually require a number of prerequisite undergraduate courses before they can embark on their graduate studies. If they meet the other requirements of the Graduate School, such students can usually be given a "full admit with prerequisite course work." The student is admitted into the graduate program but is required to complete a number of undergraduate prerequisite courses. Other constraints may be placed on such admissions, such as a minimum acceptable grade(s) for the prerequisites and perhaps a time frame for completion of the prerequisites. The exact nature of the composition of the prerequisite course work will be determined on a case by case basis. In rare cases, students who do not meet the general requirements of the graduate school, for example do not have the required minimum GPA, can be given a "provisional admit" provided their background is such that it indicates a high probability of success in the program.<br />
                                                In case of provisional admission, the program advisor may interview the candidate individually and consider the following factors:
                                            </p>

                                            <ol start="1">
                                                <li>Related background knowledge and work experience</li>
                                                <li>Classes taken since graduation</li>
                                                <li>Reference letters</li>
                                                <li>GRE&#160;scores</li>
                                            </ol>
                                        </div>
                                    </div>
                                    <div class="tab-pane" id="gpa{0}">
                                        <div class="panel-body text-left">
                                            A 3.0 undergraduate grade point average (on a 4.0 scale) in the last 90-quarter or 60-semester hours of study. In order for post-baccalaureate credit to be included in the GPA computation, the coursework must be upper division. Post-baccalaureate coursework at community colleges will not be included in the GPA used for admission. Applicants with advanced degrees from accredited institutions are generally, at the discretion of the Graduate School, considered to have met GPA requirements.
                                            <br />
                                            <p>
                                                International students must submit official translations to English of all transcripts and diplomas from all post-secondary institutions attended. Documents must be issued within two years at the time of application. All international transcripts must be submitted to World Education Service (WES) for authentication and course-by-course evaluation. To be considered official, transcripts must be in sealed envelopes prepared by the university or college; attested/certified copies prepared by the institution may be accepted if originals cannot be provided by the institution.<br />
                                                EXCEPTION:<br />
                                                Applicants attending institutions in China must request official transcripts from the Ministry-authorized verification offices listed below; transcripts directly from an institution cannot be considered official.
                                            </p>

                                            <p>
                                                <br />
                                                China Academic Degrees and Graduate Education Development Center (CDGDC)<br />
                                                Website: <a href="http://cqv.chinadegrees.cn/">cqv.chinadegrees.cn/</a>
                                            </p>

                                            <p>
                                                China Higher Education Student Information &amp;&#160;Career Center (CHESICC)<br />
                                                Website: <a href="http://chsi.com.cn">chsi.com.cn</a>
                                            </p>
                                        </div>
                                    </div>
                                    <div class="tab-pane" id="due{0}">
                                        <strong>Fall</strong>, April 15; <strong>Winter</strong>, October 1; <strong>Spring</strong>, February 1.
                                    </div>
                                </div>

                            </div>

                        </div>
                        <!-- Tabs with icons on Card End -->
"""

print(str.format(num))