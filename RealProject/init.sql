create table `Category`(
    `id` int(11) primary key not null,
    `name` varchar(128) not null,
    `icon` varchar(128),
    `add_date` datetime not null default now(),
    `pub_date` datetime not null default now()  
);

create table `Post`(
    `id` int(11) primary key not null,
    `title` varchar(128) not null,
    `desc` varchar(200),
    `has_type` enum('dratf','show'),
    `category_id` int(11) not null,
    `content` longtext not null,
    `add_date` datetime not null default now(),
    `pub_date` datetime not null default now(),
    foreign key( `category_id`) references `Category`(`id`) 
);

create table `Tag`(
    `id` int(11) primary key not null ,
    `name` char(128) not null unique
);

create table `tags`(
    `tag_id` int(11),
    `post_id` int(11),
    primary key(`tag_id`, `post_id`),
    foreign key(`tag_id`) references `Tag`(`id`),
    foreign key(`post_id`) references `Post`(`id`)
);