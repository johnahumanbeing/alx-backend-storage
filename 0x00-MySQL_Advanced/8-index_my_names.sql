-- Creates index on the table names using the first letter of name column
CREATE INDEX idx_names_first ON names (name(1));
