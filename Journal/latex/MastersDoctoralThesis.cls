%%%%%%
%%%%%%
%%
%%		fauthesis.cls
%%
%%		Version 1.0
%%		September 23, 2014
%%
%%		For support, contact Chris Beetle < cbeetle [at] physics [dot] fau [dot] edu >.
%%
%%		This LaTeX document class formats master's and doctoral theses 
%%			according to the guidelines of Florida Atlantic University (FAU).
%%		The formatting guidelines are available at << http://www.fau.edu/graduate/pubs/RevGuidelines.pdf >>.
%%		It is based on the LaTeX2e standard "report" document class.
%%
%%%%%%
%%%%%%


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{MastersDoctoralThesis}[2014/09/23 v1.0 (C. Beetle)]


%%% Degree Name Class Options
%
% Define class options to allow authors to declare their degree when loading the document class.  Default is phd.
%
\DeclareOption{ded}		{\gdef\@degree{Doctor of Education}	\gdef\@thesis{Dissertation}}
\DeclareOption{ma}		{\gdef\@degree{Master of Arts}			\gdef\@thesis{Thesis}}
\DeclareOption{ms}		{\gdef\@degree{Master of Science}		\gdef\@thesis{Thesis}}
\DeclareOption{phd}		{\gdef\@degree{Doctor of Philosophy}	\gdef\@thesis{Dissertation}}


%%% Line Spacing Class Options
%
% Define class options to double-space all text.  Final theses must be double-spaced and single-sided.  Default is doublespace.
%
\DeclareOption{singlespace}		{\AtBeginDocument{\singlespacing}}
\DeclareOption{sesquispace}		{\AtBeginDocument{\sesquispacing}}
\DeclareOption{doublespace}		{\AtBeginDocument{\doublespacing}}
%
% The following commands allow temporary reversion to single-spacing (e.g., footnotes and long quotes) and so forth.
%
\newcommand\singlespacing{\renewcommand\baselinestretch{1.00}\normalsize}
\newcommand\sesquispacing{\renewcommand\baselinestretch{1.25}\normalsize}
\newcommand\doublespacing{\renewcommand\baselinestretch{1.65}\normalsize}
%
% The following environments provide the same line-spacing control as the commands above.
%
\newenvironment{singlespace}{\begingroup\singlespacing}{\endgroup}
\newenvironment{sesquispace}{\begingroup\sesquispacing}{\endgroup}
\newenvironment{doublespace}{\begingroup\doublespacing}{\endgroup}


%%% Co-Advisor Class Options
%
% Define a class option to support two research advisors on the signature page.  Default is nocoadivsors.
%
\DeclareOption{coadvisors}		{\@coadvisorstrue}
\DeclareOption{nocoadvisors}		{\@coadvisorsfalse}
%
\newif\if@coadvisors
\@coadvisorsfalse


%%%% Dedication Style Options
%%
%% Define class options to allow a short, one-line dedication without a title on the dedication page instead of a paragraph-length dedication with a title.  Default is shortdedication.
%%
\DeclareOption{longdedication}		{\@shortdedicationfalse}
\DeclareOption{shortdedication}	{\@shortdedicationtrue}
%
\newif\if@shortdedication
\@shortdedicationtrue


%%% Table of Contents Heading Class Options
%
% Define a class option to format the headings of the Table of Contents and Lists of Tables and Figures like chapters or like the title page.
% Default is titletables, which is required by the Graduate College.
%
\DeclareOption{chaptertables}		{\@chaptertablestrue}
\DeclareOption{titletables}			{\@chaptertablesfalse}
%
\newif\if@chaptertables
\@chaptertablesfalse


%%% Appendix Heading Class Options
%
% Define a class option to format the headings for appendices and other back matter like chapters or like the title page.
% Default is titleappendices, which is required by the Graduate College.
%
\DeclareOption{chapterappendices}	{\@chapterappendicestrue}
\DeclareOption{titleappendices}		{\@chapterappendicesfalse}
%
\newif\if@chapterappendices
\@chapterappendicesfalse


%%% Chapter Heading Formatting Class Options
%
% Define class options for various formats of the heading at the top of each chapter.  Default is simplechapters.
%
\DeclareOption{classicchapters}	{%
	\AtBeginDocument{%
		\chapterheadformat
			{\sesquispacing\raggedleft}%
			{{\Large\bfseries\chaptertype\ \chapternumber\par}\vskip2.0ex}%
			{{\LARGE\bfseries\boldmath\chaptertitle\par}}%
			{\vskip5.0ex\hrule\vskip5.0ex}}}
\DeclareOption{simplechapters}	{%
	\AtBeginDocument{%
		\chapterheadformat
			{\doublespacing\centering}%
			{{\bfseries\MakeTextUppercase{\chaptertype\ \chapternumber}\par}}%
			{{\bfseries\boldmath\MakeTextUppercase{\chaptertitle}\par}}%
			{\vskip5.0ex}}}


%%% Hyperref Package Color Formatting Options
%
% Define class options to suppress coloring of embedded PDF links for print vs. online versions of the document.  Default is print.
%
\DeclareOption{print}			{%
	\gdef\fau@hypersetup{%
		\providecommand\hypersetup[1]{\relax}%		in case the hyperref package is not loaded
		\hypersetup{%							switch all link colors to black with no frame
			colorlinks=true,					% false: boxed links; true: colored links
			linkcolor=[rgb]{0.0,0.0,0.0},		% color of internal links
			citecolor=[rgb]{0.0,0.0,0.0},		% color of links to bibliography
			filecolor=[rgb]{0.0,0.0,0.0},		% color of file links
			urlcolor=[rgb]{0.0,0.0,0.0}			% color of external links
		}}}%
\DeclareOption{online}			{%
	\gdef\fau@hypersetup{\relax}}
\AtBeginDocument{%
	\providecommand\phantomsection{}%		in case the hyperref package is not loaded
	\providecommand\texorpdfstring[2]{#1}%		in case the hyperref package is not loaded
	\fau@hypersetup}%


%%% Margin Options
%
% Define class options for pre- and post-Summer 2014 margin guidelines.  Default is 2014margins.
%
\DeclareOption{2014margins}	{%
	% 1.5" inner margin
	% 1.0" outer and top
	% 0.75" bottom margin
	% 0.25" footer skip
	\gdef\fau@margins{%
		\setlength\hoffset{0pt}%
		\setlength\oddsidemargin{0.5in}%
		\setlength\textwidth{6.0in}%
		\setlength\marginparsep{0pt}%
		\setlength\marginparwidth{0pt}%
		\setlength\voffset{0pt}%
		\setlength\topmargin{0pt}%
		\setlength\headheight{0pt}%
		\setlength\headsep{0pt}%
		\setlength\textheight{9.0in}%
		\setlength\footskip{0.25in}}}
\DeclareOption{2010margins}	{%
	% 1.5" inner margin
	% 1.0" outer and top
	% 1.0" bottom margin
	% 0.5" footer skip
	\gdef\fau@margins{%
		\setlength\hoffset{0pt}%
		\setlength\oddsidemargin{0.5in}%
		\setlength\textwidth{6.0in}%
		\setlength\marginparsep{0pt}%
		\setlength\marginparwidth{0pt}%
		\setlength\voffset{0pt}%
		\setlength\topmargin{0pt}%
		\setlength\headheight{0pt}%
		\setlength\headsep{0pt}%
		\setlength\textheight{8.5in}%
		\setlength\footskip{0.5in}}}


%%% Prohibited report Class Options
%
% Disallow two options of the "report" document class because they are incompatible with FAU's formatting guidelines.
%
\DeclareOption{twocolumn}{\ClassWarning{fauthesis}{The fauthesis class does not support the twocolumn option.}}
\DeclareOption{notitlepage}{\ClassWarning{fauthesis}{The fauthesis class does not support the notitlepage option.}}


%%% Prohibited report Class Page Size Options
%
% Disallow all page size options of the "report" document class other than letterpaper
%
\DeclareOption{a4paper}{\ClassWarning{fauthesis}{The fauthesis class only supports the letterpaper page size.}}
\DeclareOption{a5paper}{\ClassWarning{fauthesis}{The fauthesis class only supports the letterpaper page size.}}
\DeclareOption{b5paper}{\ClassWarning{fauthesis}{The fauthesis class only supports the letterpaper page size.}}
\DeclareOption{legalpaper}{\ClassWarning{fauthesis}{The fauthesis class only supports the letterpaper page size.}}
\DeclareOption{executivepaper}{\ClassWarning{fauthesis}{The fauthesis class only supports the letterpaper page size.}}
\DeclareOption{landscape}{\ClassWarning{fauthesis}{The fauthesis class only supports the portrait page orientation.}}


%%% Default report Class Options and Execution
%
% Send any remaining options on to the report class, set some defaults, process any specified options, and load the report class.
%	letterpaper: 	prepare PDF on standard letter paper
%	openright: 	when printing two-sided, chapters start on odd-numbered pages
%	onecolumn: 	the text appears in a single column (required)
%	titlepage: 		print a title page (required)
%
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ExecuteOptions{doublespace,phd,nocoadvisors,titletables,shortdedication,simplechapters,titleappendices,print,2014margins}
\ProcessOptions
\LoadClass[letterpaper,openright,onecolumn,titlepage]{report}


%%% Page Geometry
%
% Set margins and test for PDFLaTeX output.  If found, then fix US Letter page style.
%
\fau@margins												% Defined by class options
%
% This is the Boolean flag that remembers if we're using PDFLaTeX
%
\newif\if@foundpdflatex
\@foundpdflatexfalse
%
% This checks carefully if the \pdfoutput command is defined, and then sets the PDF page margins.
%
{\expandafter}\expandafter\ifx\csname pdfoutput\endcsname\relax\else	% Test if \pdfoutput not defined
	\ifx\pdfoutput\relax\else 									% Test if \pdfoutput not previously tested
		\ifnum\pdfoutput > 0									% Test if \pdfoutput active
			\@foundpdflatextrue
			\setlength\pdfpageheight{11in}%
			\setlength\pdfpagewidth{8.5in}%
		\fi\fi\fi


%%% Major Document Division Formats
%
% These commands set page numbering and sectioning options for the major document divisions, including
%	\frontmatter before the first chapter, 
%	\mainmatter including all the main text, and 
%	\backmatter including any appendices, the bibliography, and perhaps sometimes an index.
%
\newcommand\frontmatter{\pagenumbering{roman}}
\newcommand\mainmatter{\pagenumbering{arabic}}
\newcommand\backmatter{\appendix}
%
\renewcommand\appendix{\par
		\setcounter{chapter}{0}%
		\setcounter{section}{0}%
		\gdef\@chapapp{\appendixname}%
		\gdef\thechapter{\@Alph\c@chapter}%
		\def\@makeschapterhead##1{%
			\noindent\raisebox{-1.0in}{%
				\begin{minipage}[t]{\hsize}%
					\doublespacing\centering%
					\parindent\z@\normalfont%
					\def\\{\protect\linebreak}%
					{\bfseries\boldmath\MakeTextUppercase{##1}\par}%
				\end{minipage}}\par\nobreak
			\vskip5.0ex}%
		\if@chapterappendices\else
			\clearpage
			\addcontentsline{toc}{chapter}{\protect\numberline{}Appendices}%
			\noindent\raisebox{-1.0in}{%
				\begin{minipage}[t]{\hsize}%
					\@titleblockstyle
					{\def\@title{Appendices}\@titleformat}%
				\end{minipage}}\par
			\vspace{5.0ex}\clearpage
			\def\@chapter[##1]##2{\ifnum \c@secnumdepth >\m@ne
					\refstepcounter{chapter}%
					\typeout{\@chapapp\space\thechapter.}%
					\addcontentsline{toc}{section}{\protect\numberline{\thechapter}##1}%
				\else
					\addcontentsline{toc}{section}{##1}%
				\fi
				\chaptermark{##1}%
				\addtocontents{lof}{\protect\addvspace{10\p@}}%
				\addtocontents{lot}{\protect\addvspace{10\p@}}%
				\if@twocolumn
					\@topnewpage[\@makechapterhead{##2}]%
				\else
					\@makechapterhead{##2}%
					\@afterheading
				\fi}
			\def\@makechapterhead##1{%
				\noindent\raisebox{0.0in}{%
					\begin{minipage}[t]{\hsize}%
						\doublespacing\centering%
						\parindent\z@\normalfont%
						\def\\{\protect\linebreak}%
						\ifnum\c@secnumdepth>\m@ne  {\bfseries\MakeTextUppercase{\@chapapp\ \thechapter}\par} \fi%
						{\bfseries\boldmath\MakeTextUppercase{##1}\par}%
					\end{minipage}}\par\nobreak
				\vskip5.0ex}%
			\renewcommand\section{%
				\@startsection{subsection}{1}{\z@}%
				{-3.5ex \@plus -1ex \@minus -.2ex}{2.3ex \@plus.2ex}%
				{\normalfont\sectionstyle}}
			\renewcommand\subsection{%
				\@startsection{subsubsection}{2}{\z@}%
				{-3.25ex\@plus -1ex \@minus -.2ex}{1.5ex \@plus .2ex}%
				{\normalfont\subsectionstyle}}
			\renewcommand\subsubsection{%
				\@startsection{paragraph}{3}{\z@}%
				{-3.25ex\@plus -1ex \@minus -.2ex}{1.5ex \@plus .2ex}%
				{\normalfont\subsubsectionstyle}}
			\renewcommand\paragraph{%
				\@startsection{subparagraph}{4}{\z@}%
				{3.25ex \@plus1ex \@minus.2ex}{-1em}%
				{\normalfont\paragraphstyle}}
			\renewcommand\subparagraph{%
				\@startsection{subparagraph}{5}{\parindent}%
				{3.25ex \@plus1ex \@minus .2ex}{-1em}%
				{\normalfont\subparagraphstyle}}
			\let\thesection\thechapter
		\fi}


%\renewcommand\appendix{\par
%		\setcounter{chapter}{0}%
%		\setcounter{section}{0}%
%		\gdef\@chapapp{\appendixname}%
%		\gdef\thechapter{\@Alph\c@chapter}%
%		\def\@makeschapterhead##1{%
%			\noindent\raisebox{-1.0in}{%
%				\begin{minipage}[t]{\hsize}%
%					\doublespacing\centering%
%					\parindent\z@\normalfont%
%					\def\\{\protect\linebreak}%
%					{\bfseries\boldmath\MakeTextUppercase{##1}\par}%
%				\end{minipage}}\par\nobreak
%			\vskip5.0ex}%
%		\if@chapterappendices\else
%			\clearpage
%			\addcontentsline{toc}{chapter}{\protect\numberline{}Appendices}%
%			\noindent\raisebox{-1.0in}{%
%				\begin{minipage}[t]{\hsize}%
%					\@titleblockstyle
%					{\def\@title{Appendices}\@titleformat}%
%				\end{minipage}}\par
%			\vspace{5.0ex}\clearpage
%			\def\@makechapterhead##1{%
%				\noindent\raisebox{0.0in}{%
%					\begin{minipage}[t]{\hsize}%
%						\doublespacing\centering%
%						\parindent\z@\normalfont%
%						\def\\{\protect\linebreak}%
%						\ifnum\c@secnumdepth>\m@ne  {\bfseries\MakeTextUppercase{\@chapapp\ \thechapter}\par} \fi%
%						{\bfseries\boldmath\MakeTextUppercase{##1}\par}%
%					\end{minipage}}\par\nobreak
%				\vskip5.0ex}%
%		\fi}


%%% Default Formats
%
% Number pages in a centered footer 
%	in arabic numerals 
%	at a fixed position, 0.75in as of Summer 2014, from the bottom of the page.
%
\pagestyle{plain}
\pagenumbering{arabic}
\raggedbottom



%%%%%%
%%%%%%
%% 
%%		AUTHOR COMMANDS
%%
%%		Each thesis author should execute the commands from the following three groups.
%%		They produce pages required by FAU with the required formatting.
%%
%%%%%%
%%%%%%



%%%
%
% Preamble Thesis, Author and Degree Information
%
% 	Every thesis should include the following information for the title, signature and abstract pages.
% 	These commands should appear in the preamble, before the \begin{document}.
%
%	\title{*thesis title*}
%	\author{*student's name*}
%	\gender{F|f|M|m}
%	\graduation{*month*}{*year*}
%	\advisor{*thesis advisor's name*}
%	\supervisor{*thesis committee member's name*}	(Repeated once for each committee member.)
%	\department{*department*}
%	\chair{*department chair's name*}
%	\college{*college*}
%	\dean{*college dean's name*}
% 	\dgc{*dean of the graduate college's name*}
%
%	Details for each command follow.
%
%%%


%%% Department
%
% This required command sets the department from which the student is graduating.
% 	e.g., \college{Department of Physics}
% Note that the word "the" is included in the template where appropriate, and should not be specified.
%
\newcommand\department[1]{\gdef\@department{#1}}
\def\@department{\ClassError{fauthesis}{\protect\department\space undefined}
	{Please specify your \protect\department\space for the signature page.}}


%%% Gender
% 
% This required command sets the student's gender, which is needed for some boilerplate text.
% 	eg., \gender{F} or \gender{M}
% Arguments can be lowercase, but there are only four allowed values.
%
\newcommand\gender[1]{%
	\ifx#1f	\gdef\@hisher{her}	\else
	\ifx#1F	\gdef\@hisher{her}	\else
	\ifx#1m	\gdef\@hisher{his}	\else
	\ifx#1M	\gdef\@hisher{his}	\else
		\ClassError{fauthesis}{\protected\gender\space unrecognized}
			{Please specify your \protect\gender\space as either F or M.}
	\fi\fi\fi\fi}
\def\@hisher{\ClassError{fauthesis}{\protect\gender\space undefined}
	{Please specify your \protect\gender\space (F or M) for the signature page.}}


%%% College
%
% This required command sets the college from which the student is graduating.
% 	e.g., \college{Charles E.~Schmidt College of Science}
% Note that the word "the" is included in the template where appropriate, and should not be specified.
%
\newcommand\college[1]{\gdef\@college{#1}}
\def\@college{\ClassError{fauthesis}{\protect\college\space undefined}
	{Please specify your \protect\college\space for the title page.}}


%%% Graduation Date
%
% This required command sets the month and year in which the student will graduate.
% 	e.g., \graduation{December}{2014}
% Note that month and year are given as separate arguments
%
\newcommand\graduation[2]{\gdef\@gradmonth{#1}\gdef\@gradyear{#2}}
\def\@gradmonth{\ClassError{fauthesis}{\protect\graduation\space date undefined}
	{Please specify your month and year of \protect\graduation\space for the title page.}}
\def\@gradyear{\ClassError{fauthesis}{\protect\graduation\space date undefined}
	{Please specify your month and year of \protect\graduation\space for the title page.}}


%%% Advisor
% 
% This required command sets the name and titles of the student's primary thesis advisor.
% 	e.g., \advisor[Dr.]{Korey Sorge}[Ph.D.]
% The first and last arguments are optional, and the defaults are as shown.
%
\newcommand\advisor[2][Dr.]{%
	\@ifnextchar[{\fau@setsignatory\@advisor[#1]{#2}}{\fau@setsignatory\@advisor[#1]{#2}[Ph.D.]}}
\def\@advisor{\ClassError{fauthesis}{\protect\advisor\space undefined}
	{Please specify your \protect\advisor\space for the signature page.}}
%
% This optional command sets the position title of the student's primary thesis advisor, 
% 	which may not always be the default "Dissertation Advisor".
%
\newcommand\advisortitle[1]{\gdef\@advisortitle{#1}}
\advisortitle{\def@ult}
%
% This optional command sets the department of the student's primary thesis advisor, 
% 	which in very rare cases may not be the default, the student's own.
%
\newcommand\advisordepartment[1]{\gdef\@advisordepartment{#1}}
\advisordepartment{\def@ult}
%
% This internal command sets various formatted commands for signatories to the thesis.
%
\def\fau@setsignatory#1[#2]#3[#4]{\gdef#1{[#2][#3][#4]}}


%%% Co-Advisor (required only for the coadvisors class option)
% 
% This optional command sets the name and titles of the student's thesis co-advisor, when applicable.
% 	e.g., \coadvisor[Dr.]{Korey Sorge}[Ph.D.]
% The first and last arguments are optional, and the defaults are as shown here.
%
\newcommand\coadvisor[2][Dr.]{%
	\@ifnextchar[{\fau@setsignatory\@coadvisor[#1]{#2}}{\fau@setsignatory\@coadvisor[#1]{#2}[Ph.D.]}}
\def\@coadvisor{\n@ne}
%
% This optional command sets the position title of the student's primary thesis advisor, 
% 	which may not always be the default that depends.
%
\newcommand\coadvisortitle[1]{\gdef\@coadvisortitle{#1}}
\coadvisortitle{\def@ult}
%
% This command sets the department of the student's thesis co-advisor, 
% 	which in rare cases may not be the default, the student's own.
%
\newcommand\coadvisordepartment[1]{\gdef\@coadvisordepartment{#1}}
\coadvisordepartment{\def@ult}
%
% The following internal code sets titles and other data for the advisor and co-advisor 
% 	depending on whether the coadvisors class option is used.
%
\AtBeginDocument{%
	\if@coadvisors										% For the coadvisors class option ...
		\expandafter\ifx\@coadvisor\n@ne						% A co-advisor is required 
			\ClassError{\protect\coadvisor\space undefined}
				{Please either specify your \protect\coadvisor\space for the signature page or remove the coadvisors class option.}
		\else
			\expandafter\ifx\@advisortitle\def@ult				% If neither advisor nor co-advisor titles are set, 
				\expandafter\ifx\@coadvisortitle\def@ult			% 	then both default to "Co-Advisor"
					\expandafter\advisortitle\expandafter{\@thesis\ Co-Advisor}
					\coadvisortitle{\s@me}
				\else										% If only a co-advisor title is set, advisor title defaults to "Advisor"
					\expandafter\advisortitle\expandafter{\@thesis\ Advisor}
				\fi
			\else											% If only an advisor title is set, co-advisor defaults to the same
				\expandafter\ifx\@coadvisortitle\def@ult  \coadvisortitle{\s@me}  \fi
			\fi
			\expandafter\ifx\@advisordepartment\def@ult			% Advisor and co-advisor departments default to student's own
				\expandafter\advisordepartment\expandafter{\@department}
				\expandafter\ifx\@coadvisordepartment\def@ult  \coadvisordepartment{\s@me}  \fi
			\else											% If advisor's is set, co-advisor's still defaults to student's own
				\expandafter\ifx\@coadvisordepartment\def@ult  \expandafter\coadvisordepartment\expandafter{\@department}  \fi
			\fi
		\fi
	\else												% For the nocoadvisors class option ...
		\expandafter\ifx\@advisortitle\def@ult  \expandafter\advisortitle\expandafter{\@thesis\ Advisor}  \fi
		\expandafter\ifx\@coadvisortitle\def@ult  \expandafter\coadvisortitle\expandafter{\@thesis\ Co-Advisor}  \fi
		\expandafter\ifx\@advisordepartment\def@ult  \expandafter\advisordepartment\expandafter{\@department}  \fi
	\fi}


%%% Other Committee Members (used once per committee member
% 
% This command sets the name and titles of the student's thesis committee members.
% 	e.g., \supervisor[Dr.]{Christopher Beetle}[Ph.D.]
% The first and last arguments are optional, and the defaults are as shown here.
% This command should be called once for each committee member, 
% 	in the order in which they should appear on the signatures page.
%
\newcommand\supervisor[2][Dr.]{\advance\@supervisors by 1%
	\@ifnextchar[{\fau@addtocommittee[#1]{#2}}{\fau@addtocommittee[#1]{#2}[Ph.D.]}}
\def\fau@addtocommittee[#1]#2[#3]{%
	\edef\@act{\noexpand\@committee={\the\@committee[#1][#2][#3]}}\@act}
%
% The following internal variable holds the list of committee members.
%
\newtoks\@committee
\@committee={}
%
% The following internal variable counts the number of committee members.
%
\newcount\@supervisors
\@supervisors=0


%%% Department Chair
% 
% This required command sets the name and titles of the student's department chair.
% 	e.g., \chair[Dr.]{Warner A.~Miller}[Ph.D.]
% The first and last arguments are optional, and the defaults are as shown here.
%
\newcommand\chair[2][Dr.]{%
	\@ifnextchar[{\fau@setsignatory\@chair[#1]{#2}}{\fau@setsignatory\@chair[#1]{#2}[Ph.D.]}}
\def\@chair{\ClassError{fauthesis}{\protect\chair\space undefined}
	{Please specify your \protect\chair\space for the signature page.}}
%
% This optional command sets the position title of the student's department chair, 
% 	which may not always be the default "Chair".
%	e.g., \chairtitle{Interim Chair} or \chairtitle{Director}
%
\newcommand\chairtitle[1]{\gdef\@chairtitle{#1}}
\chairtitle{Chair}


%%% College Dean
% 
% This required command sets the name and titles of the student's college dean.
% 	e.g., \dean[Dr.]{Gary W.~Perry}[Ph.D.]
% The first and last arguments are optional, and the defaults are as shown here.
%
\newcommand\dean[2][Dr.]{%
	\@ifnextchar[{\fau@setsignatory\@dean[#1]{#2}}{\fau@setsignatory\@dean[#1]{#2}[Ph.D.]}}
\def\@dean{\ClassError{fauthesis}{\protect\dean\space undefined}
	{Please specify your \protect\dean\space for the signature page.}}
%
% This optional command sets the position title of the student's college dean, 
% 	which may not always be the default "Dean".
%	e.g., \deantitle{Interim Dean}
%
\newcommand\deantitle[1]{\gdef\@deantitle{#1}}
\deantitle{Dean}


%%% Dean of the Graduate College
% 
% This required command sets the name and titles of the Dean of the Graduate College.
% 	e.g., \dgc[Dr.]{Deborah L.~Floyd}[Ed.D.]
% The first and last arguments are optional, and the defaults are as shown here.
%
\newcommand\dgc[2][Dr.]{%
	\@ifnextchar[{\fau@setsignatory\@dgc[#1]{#2}}{\fau@setsignatory\@dgc[#1]{#2}[Ph.D.]}}
\def\@dgc{\ClassError{fauthesis}{\protect\dgc\space undefined}
	{Please specify the Dean of the Graduate College for the signature page.}}
%
% This optional command sets the position title of the Dean of the Graduate College, 
% 	which may not always be the default "Dean".
%	e.g., \dgctitle{Interim Dean}
%
\newcommand\dgctitle[1]{\gdef\@dgctitle{#1}}
\dgctitle{Dean}



%%%
% 
% Front Matter Page Commands
%
% 	Every thesis should execute the following commands after the \begin{document}.
%	Each produces an entire formatted page from information specified in the preamble.
%
%	\maketitle									(Formatted title page.)
%	\makecopyright								(Formatted copyright page.)
%	\makesignature								(Formatted signatures page.)
%
%	Details for each command follow.
%
%%%


%%% Frontmatter Counter
%
% The preliminary pages in a thesis must appear in a specific order.
% This counter helps produce warnings if that order is not used.
%
\newcount\fau@frontstage
\fau@frontstage=0


%%% Title Page (required)
%
% This redefines the LaTeX title page to show the information required by FAU.
%
\renewcommand\maketitle{\clearpage
	\ifnum\fau@frontstage=0\else  \ClassWarning{fauthesis}{\protect\maketitle\space out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The title page of an FAU thesis \textit{must} appear 
					at the front of the document. 
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\thispagestyle{titlepage}%
	\noindent\raisebox{-1.0in}{%
		\begin{minipage}[t]{\hsize}%
			\@titleblockstyle
			{\def\\{\protect\linebreak}\@titleformat}\\
			by\\
			\@author
		\end{minipage}}\par%
	\vspace{2.0in}%
	\begin{center}%
		A \@thesis\ Submitted to the Faculty of\\
		The \@college\\
		in Partial Fulfillment of the Requirements for the Degree of\\
		\@degree
	\end{center}%
	\clearpage}
%
% Define a page style for the title page, putting the University address in the footer, exactly 1.0in from the bottom.
%
\newcommand\ps@titlepage{\let\@oddhead\@empty%
	\setlength\footskip{9.0in}%
	\addtolength\footskip{-\textheight}%
	\def\@oddfoot{\hfill
		\raisebox{0pt}[0pt][0pt]{\parbox[b]{6in}{\centering
				Florida Atlantic University\\
				Boca Raton, FL\\
				\@gradmonth\ \@gradyear}}}\hfill}


%%% Copyright Page (required)
%
% This sets a page with the copyright information.
% By default, it uses the author's name and graduation year from the preamble, 
%	but these may be overridden by specifying an optional argument 
%	e.g., \makecopyright[*anything*]
%
\newcommand\makecopyright[1][\@gradyear\ by \@author]{\clearpage
	\advance\fau@frontstage by 1
	\ifnum\fau@frontstage=1\else  \ClassWarning{fauthesis}{\protect\makecopyright\space out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The copyright page of an FAU thesis \textit{must} appear 
					between the title and signature pages.
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\noindent\raisebox{-3.5in}{%
		\begin{minipage}[t]{\hsize}\centering
			Copyright #1
		\end{minipage}}%
	\clearpage}


%%% Signature Page (required)
%
% This sets a page for the signatures of the student's committee and University officials.
% It uses the information from the preamble.
%
\newcommand\makesignature{\clearpage
	\advance\fau@frontstage by 2
	\ifnum\fau@frontstage=3\else  \ClassWarning{fauthesis}{\protect\makesignature\space out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The signature page of an FAU thesis \textit{must} appear 
					between the title and acknowledgements pages.
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\noindent\raisebox{-1.0in}{%
		\begin{minipage}[t]{\hsize}%
			\@titleblockstyle
			{\def\\{\protect\linebreak}\@titleformat}\\
			by\\
			\@author
		\end{minipage}}\par\null\par
	\noindent\begin{minipage}[t]{\hsize}\singlespacing
		\ifx\@signatureblock\relax
			This \expandafter\MakeLowercase{\@thesis} was prepared under the direction of the candidate's 
			\if@coadvisors
				\expandafter\ifx\@coadvisortitle\s@me
					\expandafter\MakeLowercase{\@advisortitle}s, 
					\expandafter\ifx\@coadvisordepartment\s@me
						\expandafter\pretitle\@advisor\ and \expandafter\pretitle\@coadvisor, \@department, 
					\else
						\expandafter\pretitle\@advisor, \@advisordepartment, and
						\expandafter\pretitle\@coadvisor, \@coadvisordepartment, 
					\fi
				\else
					\expandafter\MakeLowercase{\@advisortitle}, \expandafter\pretitle\@advisor, \@advisordepartment, and 
					\expandafter\MakeLowercase{\@coadvisortitle}, \expandafter\pretitle\@coadvisor, 
					\expandafter\ifx\@coadvisordepartment\s@me  \@advisordepartment,  \else  \@coadvisordepartment,  \fi
				\fi
			\else
				\expandafter\MakeLowercase{\@advisortitle}, \expandafter\pretitle\@advisor, \@advisordepartment, 
			\fi
			and has been approved by the members of \@hisher\ supervisory committee.  
			It was submitted to the faculty of the \@college\ and was accepted in partial fulfillment 
			of the requirements for the degree of \@degree.
		\else  \@signatureblock  \fi
	\end{minipage}\par\null\par
	\noindent\null\hfill\begin{minipage}[t]{2.875in}\singlespacing
		SUPERVISORY COMMITTEE:\par
	\end{minipage}\vfill
	\noindent\null\hfill\showsignature{2.875in}{\@advisor}{\@advisortitle}\vfill
	\expandafter\ifx\@coadvisor\n@ne\else
		\expandafter\ifx\@coadvisortitle\s@me
			\noindent\hfill\showsignature{2.875in}{\@coadvisor}{\@advisortitle}\vfill
		\else
			\noindent\hfill\showsignature{2.875in}{\@coadvisor}{\@coadvisortitle}\vfill
		\fi
	\fi
	\begingroup
	\loop\ifnum\@supervisors>0
		\getthissupervisor
		\noindent\null\hfill\showsignature{2.875in}{\@thissupervisor}{\relax}\vfill
	\repeat\vskip-\lastskip
	\endgroup
	\@signaturepush
	\expandafter\ifx\@coadvisor\n@ne
		\ifnum\@supervisors < 3  \vfill  \else  \vskip-3.0ex  \fi
	\else
		\ifnum\@supervisors < 2  \vfill  \else  \vskip-3.0ex  \fi
	\fi
	\noindent\showsignature{2.875in}{\@chair}{\@chairtitle, \@department}\vfill
	\noindent\showsignature{2.875in}{\@dean}{\@deantitle, The \@college}\vfill
	\noindent\showsignature{2.875in}{\@dgc}{\@dgctitle, Graduate College}\hfill
		\begin{minipage}[t]{2.0in}\singlespacing%\@signaturesize
			\parbox[b]{\hsize}{\null\hrulefill}\par\vskip-0.5ex
			Date\par
		\end{minipage}
	\clearpage}
%
% This command typesets a single signature box: 
%	of width #1, 
%	containing the signature of #2, 
%	whose title is #3, which is suppressed if #3 = \relax.
% This command is internal, and should not be called directly by the author.
%
\newcommand\showsignature[3]{%
	\begin{minipage}[t]{#1}\singlespacing%\@signaturesize
		\parbox[b]{\hsize}{\null\hrulefill}\par\vskip-0.5ex
		\expandafter\posttitle#2\par
		\ifx#3\relax\else  #3\par  \fi 	% use \rlap{#3}\par instead of #3\par to allow title to overflow
	\end{minipage}}
%
% This command pulls the first supervisor on the \@committee list into the command \@thissupervisor.
% This command is internal and should not be called directly by the author.
%
\newcommand\getthissupervisor{\expandafter\fau@getthissupervisor\the\@committee\st@p}
\def\fau@getthissupervisor[#1][#2][#3]#4\st@p{%
	\advance\@supervisors by -1%
	\@committee={#4}%
	\def\@thissupervisor{[#1][#2][#3]}}
%
% These commands set thesis signatories with titles either before (e.g., Dr.) or after (e.g., Ph.D.) the name.
%
\def\pretitle[#1][#2][#3]{#1~#2}
\def\posttitle[#1][#2][#3]{#2, #3{}}
%
% This optional environment overrides the default text above the signatures.
% It should be used in the preamble, and only if the default text is clearly incorrect.
%
\newenvironment{signaturetext}{\begingroup\@temptokena={}\@readblock}
	{\edef\@act{\noexpand\gdef\noexpand\@signatureblock{\the\@temptokena}}\@act\endgroup}
%
% This internal command supports the signaturetext environment.
% It reads the contents of the environment into a token list, which then is stored for later use.
%
\long\def\@readblock#1\end#2{%
	\edef\@test{\expandafter\noexpand\csname#2\endcsname}%
	\expandafter\ifx\@test\signaturetext
		\toks@={#1}%
		\def\n@xt{\end{signaturetext}}%
	\else
		\toks@={#1 \end{#2}}%
		\let\n@xt\@readblock%
	\fi
	\edef\@act{\noexpand\@temptokena={\the\@temptokena\the\toks@}}\@act\n@xt}
%
% This default value produces the default boilerplate text on the signature page.
%
\let\@signatureblock\relax
%
% This optional command modifies the vertical space between the two signature blocks: 
% 		the block on the upper right with committee signatures, 
% 		and the block on the lower left with administration signatures.
% 	The argument is a pure number.
% 	Positive values add whitespace, while negative values allow overlap.
\newcommand\signaturepush[1]{\gdef\@signaturepush{\vskip 0pt plus #1fill\relax}\relax}
%
% By default no space is added or subtracted.
%
\let\@signaturepush\relax



%%%
% 
% Front Matter Page Environments
%
% 	Every thesis should execute the following commands after the \begin{document}.
%	Each produces an entire formatted page from information specified in the preamble.
%
%	\begin{vita} 								(Author's vita.  Optional.)
%		... 
%	\end{vita}
%	\begin{ackowledgements} 					(Author's acknowledgements.)
%		... 
%	\end{ackowledgements}
%	\begin{abstract} 							(Abstract for thesis.)
%		... 
%	\end{abstract}
%	\begin{dedication} 							(Dedication of thesis.  Optional.)
%		... 
%	\end{dedication}
%
%	Details for each environment follow.
%
%%%


%%% Vita (optional)
%
% This sets a page for the student's vita, which is optional.
% The title for the page may be specified as an optional argument, 
%	as in \begin{vita}[Vita] ...
% Support to put this at the end of the thesis may be added in a later revision of the class.
%
\newenvironment{vita}[1][Vita]{\clearpage\setlength\parindent{0.5in}%
	\ifnum\fau@frontstage=3\else  \ClassWarning{fauthesis}{vita environment out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The (optional) vita page of an FAU thesis \textit{must} appear 
					either between the signature and acknowledgements pages 
					or at the back of the document.
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\noindent\raisebox{-1.0in}{%
		\begin{minipage}[t]{\hsize}%
			\@titleblockstyle
			{\def\@title{#1}\@titleformat}%
		\end{minipage}}\par
	\vspace{5.0ex}}{\clearpage}


%%% Acknowledgements (required)
%
% This sets a page for the student's acknowledgements.
% The title for the page may be specified as an optional argument, 
%	as in \begin{acknowledgements}[Acknowledgments] ...
%
\newenvironment{acknowledgements}[1][Acknowledgements]{\clearpage\setlength\parindent{0.5in}%
	\global\advance\fau@frontstage by 4
	\ifnum\fau@frontstage=7\else  \ClassWarning{fauthesis}{acknowledgements environment out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The acknowledgements page of an FAU thesis \textit{must} appear 
					between the signature and abstract pages.
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\noindent\raisebox{-1.0in}{%
		\begin{minipage}[t]{\hsize}%
			\@titleblockstyle
			{\def\@title{#1}\@titleformat}%
		\end{minipage}}\par
	\vspace{5.0ex}}{\clearpage}


%%% Abstract (required)
%
% This sets a page for the abstract of the thesis.
% It also uses information specified in the preamble.
% The title for the page may be specified as an optional argument, 
%	as in \begin{abstract}[Abstract] ...
% It is the student's responsibility to make sure the abstract complies with the University's word count limits.
%
\renewenvironment{abstract}{\clearpage\setlength\parindent{0.5in}%
		\global\advance\fau@frontstage by 8
		\ifnum\fau@frontstage=15\else  \ClassWarning{fauthesis}{abstract environment out of order}%
			\noindent\raisebox{0pt}[0pt][0pt]{%
				\begin{minipage}[t]{\hsize}\singlespacing
					\textbf{Warning:} The abstract page(s) of an FAU thesis \textit{must} appear 
						between the acknowledgements page and the table of contents.
						Please revise your \LaTeX\ source accordingly.
				\end{minipage}}\vskip-\baselineskip
		\fi
		\noindent\raisebox{-1.0in}{%
		\begin{minipage}[t]{\hsize}%
			\@titleblockstyle
			{\def\@title{Abstract}\@titleformat}%
		\end{minipage}}\par
		\vspace{5.0ex}%
		\begin{list}{}{
			\if@coadvisors
				\expandafter\ifx\@coadvisortitle\s@me
					\setbox\@tempboxa\hbox{\@advisortitle s:}\@tempdima\wd\@tempboxa
				\else
					\setbox\@tempboxa\hbox{\@advisortitle:}\@tempdima\wd\@tempboxa
					\setbox\@tempboxa\hbox{\@coadvisortitle:}%
					\ifdim\wd\@tempboxa > \@tempdima  \@tempdima\wd\@tempboxa  \fi
				\fi
			\else
				\setbox\@tempboxa\hbox{\@advisortitle:}\@tempdima\wd\@tempboxa
			\fi
			\advance\@tempdima 1em%
			\setlength{\leftmargin}{\@tempdima}		\setlength{\rightmargin}{0pt}
			\setlength{\itemindent}{0pt}			\setlength{\listparindent}{0pt}
			\setlength{\labelwidth}{\leftmargin}		\setlength{\labelsep}{0pt}
			\setlength{\topsep}{0pt}				\setlength{\partopsep}{0pt}
			\setlength{\itemsep}{0pt}				\setlength{\parsep}{0pt}}
			\item[Author: \hfill] \@author\par
			\item[Title: \hfill] {%
				\@tempdima\hsize\advance\@tempdima-\leftmargin\relax
				\parbox[t]{\@tempdima}{\singlespacing\raggedright\def\\{{}}\@title\par\null}}\par
			\item[Institution: \hfill] Florida Atlantic University
			\if@coadvisors
				\expandafter\ifx\@coadvisortitle\s@me
					\item[\@advisortitle s: \hfill] {%
						\@tempdima\hsize\advance\@tempdima-\leftmargin\relax
						\parbox[t]{\@tempdima}{\singlespacing\raggedright
							\expandafter\pretitle\@advisor\par
							\expandafter\pretitle\@coadvisor\par
							\null}}\par
				\else
					\item[\@advisortitle: \hfill] \expandafter\pretitle\@advisor
					\item[\@coadvisortitle: \hfill] \expandafter\pretitle\@coadvisor
				\fi
			\else
				\item[\@advisortitle: \hfill] \expandafter\pretitle\@advisor
			\fi
			\item[Degree: \hfill] \@degree
			\item[Year: \hfill] \@gradyear
		\end{list}\par\nointerlineskip
		\vspace{5.0ex}}
	{\clearpage}


%%% Dedication (optional)
%
% This sets a page dedicating the thesis, which is optional.
%
\newenvironment{dedication}{\clearpage
	\thispagestyle{empty}%
	\ifnum\fau@frontstage=15\else  \ClassWarning{fauthesis}{dedication environment out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The dedication page of an FAU thesis \textit{must} appear 
					between the abstract page(s) and the table of contents.
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\if@shortdedication
		\noindent\vspace{3.2in}\par
		\noindent\begin{minipage}[t]{\hsize}\centering\normalfont\slshape
			\def\\{\protect\linebreak}%
	\else
		\noindent\raisebox{-1.0in}{%
			\begin{minipage}[t]{\hsize}%
				\@titleblockstyle
				{\def\@title{Dedication}\@titleformat}%
			\end{minipage}}\par
		\vspace{5.0ex}%
		\noindent\begin{minipage}[t]{\hsize}\normalfont
			\def\\{\protect\linebreak}%
			\setlength\parindent{0.5in}%
			\indent\ignorespaces
	\fi}
	{\end{minipage}\clearpage}
%
% This offers a shorter command, instead of an environment, for a one-line dedication.
%
\newcommand\dedicate[1]{\begin{dedication}#1\end{dedication}}



%%%
% 
% Front Matter Document Information
%
% 	Every thesis should execute the following commands after the \begin{document}.
%	Each produces a formatted section from information extracted from the document.
%
%	\tableofcontents
% 	\listoffigures
% 	\listoftables
%
%	These are currently given a standard format by the class author, 
%		which is based on the format for chapter headings from the main matter.
% 	Options to allow more control to document authors may be included in subsequent versions of the class.
%
%%%


%%% Table of Contents (required)
%
% This modifies the default LaTeX \tableofcontents command to: 
% 	incorporate a check for the proper page ordering, and 
% 	use the thesis title in the title block style for the heading, 
% 		unless the chaptertables class option is in effect.
%
\renewcommand\tableofcontents{\cleardoublepage
	\advance\fau@frontstage by 16
	\ifnum\fau@frontstage=31\else  \ClassWarning{fauthesis}{\protect\tableofcontents\space out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The table of contents of an FAU thesis \textit{must} appear 
					between the abstract and the list of tables. 
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\if@chaptertables
		\chapter*{\contentsname\@mkboth{\contentsname}{\contentsname}}%
	\else
		\noindent\raisebox{-1.0in}{%
			\begin{minipage}[t]{\hsize}%
				\@titleblockstyle
				{\def\\{\protect\linebreak}\@titleformat}%
			\end{minipage}}\par%
		\vspace{5.0ex}%
		\relax
		\@mkboth{\contentsname}{\contentsname}%
	\fi
	\@starttoc{toc}\cleardoublepage}
%
% This modifies the default LaTeX format for chapter titles in the table of contents items to: 
% 	set each chapter title single spaced, 
% 	use bold math within chapter titles, 
% 	include a blank line after the chapter title to double-space between items, 
% 	include leaders to the page number, and 
% 	set the page number in normal font, rather than bold.
%
\renewcommand*\l@chapter[2]{%
	\ifnum \c@tocdepth >\m@ne
		\addpenalty{-\@highpenalty}%
		\vskip 1.0em \@plus\p@
		\setlength\@tempdima{1.5em}%
		\begingroup
			\singlespacing\def\\{{}}%
			\parindent \z@ \rightskip \@tocrmarg
			\parfillskip -\@tocrmarg
			\leavevmode\normalfont\bfseries\boldmath
			\advance\leftskip\@tempdima
			\hskip -\leftskip
			#1\nobreak
			\leaders\hbox{\normalfont$\m@th\mkern\@dotsep mu\hbox{.}\mkern \@dotsep mu$}\hfill\nobreak
			\hb@xt@\@pnumwidth{\hss\normalfont #2}\par
			\vspace{1.7ex}%
			\penalty\@highpenalty
		\endgroup
	\fi}
%
% This modifies the default LaTeX format for other items in the table of contents to: 
% 	set each item title single-spaced.
%
\def\@dottedtocline#1#2#3#4#5{%
	\ifnum #1>\c@tocdepth \else
		\vskip \z@ \@plus.2\p@
		{\singlespacing\def\\{{}}\leftskip #2\relax \rightskip \@tocrmarg \parfillskip -\rightskip
		\parindent #2\relax\@afterindenttrue
		\interlinepenalty\@M
		\leavevmode
		\@tempdima #3\relax
		\advance\leftskip \@tempdima \null\nobreak\hskip -\leftskip
		{#4}\nobreak
		\leaders\hbox{$\m@th
			\mkern \@dotsep mu\hbox{.}\mkern \@dotsep
			mu$}\hfill
		\nobreak
		\hb@xt@\@pnumwidth{\hfil\normalfont\normalcolor #5}%
		\par
		\vspace{1.7ex}}%
	\fi}


%%% List of Tables (required if there are tables)
%
% This modifies the default LaTeX \listoftables command to: 
% 	incorporate a check for the proper page ordering, and 
% 	use the title block style for the heading, 
% 		unless the chaptertables class option is in effect.
%
\renewcommand\listoftables{\cleardoublepage
	\advance\fau@frontstage by 32
	\ifnum\fau@frontstage=63\else  \ClassWarning{fauthesis}{\protect\listoftables\space out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The list of tables of an FAU thesis \textit{must} appear 
					between the table of contents and the list of figures. 
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\phantomsection
	\if@chaptertables
		\chapter*{\listtablename\@mkboth{\listtablename}{\listtablename}}%
	\else
		\noindent\raisebox{-1.0in}{%
			\begin{minipage}[t]{\hsize}%
				\@titleblockstyle
				{\def\@title{\listtablename}\@titleformat}%
			\end{minipage}}\par%
		\vspace{5.0ex}%
		\@mkboth{\listtablename}{\listtablename}%
	\fi
	\addcontentsline{toc}{chapter}{\protect\numberline{}\listtablename}%
	\@starttoc{lot}\cleardoublepage}
%
% This advances the frontmatter counter without including a list of tables for theses containing no tables.
%
\newcommand\nolistoftables{%
	\advance\fau@frontstage by 32
	\ifnum\fau@frontstage=63\else  \ClassWarning{fauthesis}{\protect\nolistoftables\space out of order}%
		\cleardoublepage
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The list of tables in an FAU thesis \textit{must} appear 
					between the table of contents and the list of figures.  
					The command to omit the list of tables must appear in the same position.  
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
		\cleardoublepage
	\fi}


%%% List of Figures (required if there are figures)
%
% This modifies the default LaTeX \listoffigures command to: 
% 	incorporate a check for the proper page ordering, and 
% 	use the title block style for the heading, 
% 		unless the chaptertables class option is in effect.
%
\renewcommand\listoffigures{\cleardoublepage
	\advance\fau@frontstage by 64
	\ifnum\fau@frontstage=127\else  \ClassWarning{fauthesis}{\protect\listoffigures\space out of order}%
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The list of figures of an FAU thesis \textit{must} appear 
					between the list of tables and the beginning of the manuscript. 
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
	\fi
	\phantomsection
	\if@chaptertables
		\chapter*{\listfigurename\@mkboth{\listfigurename}{\listfigurename}}%
	\else
		\noindent\raisebox{-1.0in}{%
			\begin{minipage}[t]{\hsize}%
				\@titleblockstyle
				{\def\@title{\listfigurename}\@titleformat}%
			\end{minipage}}\par%
		\vspace{5.0ex}%
		\@mkboth{\listfigurename}{\listfigurename}%
	\fi
	\addcontentsline{toc}{chapter}{\protect\numberline{}\listfigurename}%
	\@starttoc{lof}\cleardoublepage}
%
% This advances the frontmatter counter without including a list of figures for theses containing no figures.
%
\newcommand\nolistoffigures{%
	\advance\fau@frontstage by 64
	\ifnum\fau@frontstage=127\else  \ClassWarning{fauthesis}{\protect\nolistoffigures\space out of order}%
		\cleardoublepage
		\noindent\raisebox{0pt}[0pt][0pt]{%
			\begin{minipage}[t]{\hsize}\singlespacing
				\textbf{Warning:} The list of figures of an FAU thesis \textit{must} appear 
					between the list of tables and the beginning of the manuscript. 
					The command to omit the list of figures must appear in the same position.
					Please revise your \LaTeX\ source accordingly.
			\end{minipage}}\vskip-\baselineskip
		\cleardoublepage
	\fi}



%%%%%%
%%%%%%
%% 
%%		INTERNAL FORMATTING COMMANDS
%%
%%		The following commands are used to format section headings and so forth.
%%		Individual authors probably do not need to study these carefully...
%%
%%%%%%
%%%%%%


%%% Title Block Formatting
%
% This command specifies how the title of the thesis is to be formatted.
% Definitely best not to change this.
%
\newcommand\titleheadformat[2]{%
	\gdef\@titleblockstyle{#1}%
	\gdef\@titleformat{#2}}
%
% The default title block style is bold and all caps, except for math.
% 
\titleheadformat
	{\centering}%
	{{\bfseries\MakeTextUppercase{\@title}}}%
%
% This command converts text to all caps, excluding: 
% 	anything set in inline math mode, and 
% 	anything enclosed in a \FixCase command.
% 
\newcommand\MakeTextUppercase[1]{%
	\begingroup
	\def\({$}\let\)\(%
	\protected@edef\@act{\endgroup			
		\noexpand\@maketextuppercase#1$\noexpand\@stop$\noexpand\@endtextuppercase}%
	\@act}
%
\def\@maketextuppercase#1$#2#3$#4\@endtextuppercase{%
	\uppercase{#1}%
	\ifx\@stop#2\else%
		$#2#3$%
		\@maketextuppercase#4\@endtextuppercase%
	\fi}
%
\newcommand\FixCase[1]{#1}



%%% Chapter Heading Formatting
%
% This command offers a simple, but somewhat flexible way to format chapter headings, as 
% 	a paragraph formatted according to #1, 
% 	with the chapter label (e.g., Chapter 1) set by #2, 
% 	and the chapter title (e.g., My First Chapter) set by #3, and 
% 	followed by space or rule set by #4.
% The following standard variables may be used: 
% 	\chaptertype is the type of chapter (i.e., Chapter or Appendix)
% 	\chapternumber is the number for the chapter (e.g., 1 or A)
% 	\chaptertitle is the title text for the chapter
%
\newcommand\chapterheadformat[4]{%
	\gdef\@chapterblockstyle{#1}%
	\gdef\@chapternumberformat{#2}%
	\gdef\@chaptertitleformat{#3}%
	\gdef\@chapterblockskip{#4}}
%
% This modifies the default LaTeX chapter headings using the format set above.
%
\def\@makechapterhead#1{%
	\noindent\raisebox{-1.0in}{%
		\begin{minipage}[t]{\hsize}%
			\def\chaptertype{\@chapapp}%
			\def\chapternumber{\thechapter}%
			\def\chaptertitle{#1}%
			\@chapterblockstyle%
			\parindent\z@\normalfont%
			\def\\{\protect\linebreak}%
			\ifnum\c@secnumdepth>\m@ne  \@chapternumberformat  \fi%
			\@chaptertitleformat%
		\end{minipage}}\par\nobreak
		\@chapterblockskip}
%
% This does the same for unnumbered chapters.
%
\def\@makeschapterhead#1{%
	\noindent\raisebox{-1.0in}{%
		\begin{minipage}[t]{\hsize}%
			\def\chaptertype{\@chapapp}%
			\def\chapternumber{\thechapter}%
			\def\chaptertitle{#1}%
			\@chapterblockstyle%
			\parindent\z@\normalfont%
			\def\\{\protect\linebreak}%
			\@chaptertitleformat%
		\end{minipage}}\par\nobreak
		\@chapterblockskip}


%%% Section Heading Formatting
%
% The following commands will be executed to format the headings for sections, subsections, etc.
% Each, in principle, can end with a command that takes a single argument.
%
\newcommand\sectionstyle{\normalsize\bfseries\boldmath\MakeTextUppercase}
\newcommand\subsectionstyle{\normalsize\bfseries}
\newcommand\subsubsectionstyle{\normalsize\itshape}
\newcommand\paragraphstyle{\small\bfseries}
\newcommand\subparagraphstyle{\small\bfseries}
%
% These redefine the default LaTeX headings for sections, subsections, etc. to use the formats above.
%
\renewcommand\section{%
	\@startsection{section}{1}{\z@}%
	{-3.5ex \@plus -1ex \@minus -.2ex}{2.3ex \@plus.2ex}%
	{\normalfont\sectionstyle}}
\renewcommand\subsection{%
	\@startsection{subsection}{2}{\z@}%
	{-3.25ex\@plus -1ex \@minus -.2ex}{1.5ex \@plus .2ex}%
	{\normalfont\subsectionstyle}}
\renewcommand\subsubsection{%
	\@startsection{subsubsection}{3}{\z@}%
	{-3.25ex\@plus -1ex \@minus -.2ex}{1.5ex \@plus .2ex}%
	{\normalfont\subsubsectionstyle}}
\renewcommand\paragraph{%
	\@startsection{paragraph}{4}{\z@}%
	{3.25ex \@plus1ex \@minus.2ex}{-1em}%
	{\normalfont\paragraphstyle}}
\renewcommand\subparagraph{%
	\@startsection{subparagraph}{5}{\parindent}%
	{3.25ex \@plus1ex \@minus .2ex}{-1em}%
	{\normalfont\subparagraphstyle}}


%%% Caption Formatting
%
% This modifies the default LaTeX format for figure and table captions.
% 	Single-line captions are set centered under the figure.
% 	Multi-line captions are set centered in a paragraph of width \capwidth.
%
\long\def\@makecaption#1#2{%
	\vskip\abovecaptionskip
	\sbox\@tempboxa{\small{\bfseries #1\/}: #2}%
	\ifdim \wd\@tempboxa > \capwidth
		\@tempdima=\textwidth%
		\advance\@tempdima by -\capwidth%
		\advance\leftskip by 0.5\@tempdima%
		\advance\rightskip by 0.5\@tempdima%
		\singlespacing
		{\bfseries #1\/}: #2\par
	\else
		\hbox to\hsize{\hfil\box\@tempboxa\hfil}%
	\fi
	\vskip\belowcaptionskip}
%
% The default \capwidth is 80% of the \textwidth.
%
\newlength{\capwidth}
\setlength{\capwidth}{0.8\textwidth}


%%% Footnote Formatting
%
% Make footnotes single-spaced.
%
\renewcommand\@makefntext[1]{\singlespacing%
	\footnotesize  \parindent 1em%
	\noindent\hb@xt@1.8em{\hss\@makefnmark}#1}


%%% Black Quote Formatting
%
% Make block quotes single-spaced.
%
\renewenvironment{quotation}
               {\par\list{}{\listparindent 1.5em%
                        \itemindent    \listparindent
                        \rightmargin   \leftmargin
                        \parsep        \z@ \@plus\p@}%
                \singlespacing\item\relax}
               {\par\endlist\ignorespaces}


%%% Bibliography Formatting
%
% This modifies the default LaTeX thebibliography environment to: 
% 	appear in the table of contents, and 
% 	list individual items single-spaced.
%
\renewenvironment{thebibliography}[1]{%
	\chapter*{\bibname\@mkboth{\bibname}{\bibname}}%
	\addcontentsline{toc}{chapter}{\protect\numberline{}\bibname}%
	\begin{singlespace}
	\list{\@biblabel{\@arabic\c@enumiv}}%
		{\settowidth\labelwidth{\@biblabel{#1}}%
			\leftmargin\labelwidth\advance\leftmargin\labelsep
			\@openbib@code
			\usecounter{enumiv}\let\p@enumiv\@empty
			\renewcommand\theenumiv{\@arabic\c@enumiv}}%
		\sloppy  \clubpenalty4000  \@clubpenalty\clubpenalty  \widowpenalty4000%
		\sfcode`\.\@m}
	{\def\@noitemerr{\@latex@warning{Empty `thebibliography' environment}}%
		\endlist\end{singlespace}}