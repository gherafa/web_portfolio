show databases;
use heroku_6a634f65adc2eaa;
use myflaskapp;
show tables;
select * from articles;
select * from users;
drop TABLE articles;


CREATE TABLE articles (
  id int(11) NOT NULL,
  title varchar(255) DEFAULT NULL,
  author varchar(100) DEFAULT NULL,
  body text DEFAULT NULL,
  create_date timestamp NOT NULL DEFAULT current_timestamp()
);

-- Dumping data for table `articles`

INSERT INTO articles (id, title, author, body, create_date) VALUES
(5, 'BANJIR DI GEDEBAGE', 'fara', '<p>ADA BANJIR BEUL GELO DI GEDEBAGE!</p>\r\n', '2020-02-13 11:21:00'),
(6, 'BANJIR DI CIMAHI', 'fawfaw', '<p>BANJIR CUY, KACAU, SETINGGI PAHA KUCING.</p>\r\n', '2020-02-13 11:38:16');

-- --------------------------------------------------------

--
-- Table structure for table `users`
-- 

CREATE TABLE users (
  id int(11) NOT NULL,
  name varchar(100) DEFAULT NULL,
  email varchar(100) DEFAULT NULL,
  username varchar(30) DEFAULT NULL,
  password varchar(100) DEFAULT NULL,
  register_date timestamp NOT NULL DEFAULT current_timestamp()
)

--
-- Dumping data for table `users`
--

INSERT INTO users (id, name, email, username, password, register_date) VALUES
(1, 'ghe', 'ghe@gmail.com', 'rafa', '$5$rounds=535000$2Jp5WUyh90d3f6Tl$QtDqkoAv41VdmIOcC9q7zGlRRRUFu.AD4jL9HKTyxG.', '2020-01-29 04:12:06'),
(11, 'rahmat', 'rahmat@gmail.com', 'rahmat', '$5$rounds=535000$wSOX4HqSRpKfEQXf$NGwT7HRMcPBHWvXgtGipncMNCzwYmKUQKzJgO0ae9N.', '2020-01-29 04:54:47'),
(12, 'fauzi', 'fauzi@gmail.com', 'fawfaw', '$5$rounds=535000$D09h701dn34ThdEB$HvOXVOud3YTq/7MYFsXecnTu5I8nJH2otUQqR0Nz/O6', '2020-01-29 05:01:37'),
(15, 'Gheo RF', 'lagoonjack@gmail.com', 'gherafa', '$5$rounds=535000$39xqtaUCiTDcUvGw$K4j8oQtmjrxc1N2GJ6L8euS0FPO11zukAgZ5ZyKC5pC', '2020-02-13 05:29:35');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articles`
--
ALTER TABLE articles
  ADD PRIMARY KEY (id);

--
-- Indexes for table `users`
--
ALTER TABLE users
  ADD PRIMARY KEY (id);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `articles`
--
ALTER TABLE articles
  MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE users
  MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
