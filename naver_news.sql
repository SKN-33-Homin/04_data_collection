create table naver_news (
    id int primary key auto_increment,
    title varchar(512),
    originallink varchar(512),
    link varchar(512),
    description text,
    pub_date varchar(512),
    created_at datetime default (current_timestamp)
);

# link 컬럼에 unique 제약조건 추가(중복 방지)
alter table naver_news
add constraint uq_naver_news_link unique (link);