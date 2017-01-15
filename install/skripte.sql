BEGIN;
--
-- Create model Car
--
CREATE TABLE "por_car" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fuel_consumption" decimal NOT NULL, "brand" varchar(20) NOT NULL, "car_model" varchar(20) NOT NULL, "year" integer , "kilometers" integer, "rotation_speed" integer, "image" blob);
--
-- Create model Comments
--
CREATE TABLE "por_comments" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "comment" text NOT NULL, "pub_date" datetime NOT NULL, "author_id" integer NULL REFERENCES "auth_user" ("id"), "car_id" integer NOT NULL REFERENCES "por_car" ("id"));
--
-- Create model Profile
--
CREATE TABLE "por_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "pic" blob, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"));
--
-- Add field owner to car
--
ALTER TABLE "por_car" RENAME TO "por_car__old";
CREATE TABLE "por_car" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fuel_consumption" decimal NOT NULL, "brand" varchar(20) NOT NULL, "car_model" varchar(20) NOT NULL, "year" integer NOT NULL, "kilometers" integer NOT NULL, "rotation_speed" integer NOT NULL, "image" blob NOT NULL, "owner_id" integer NULL REFERENCES "por_profile" ("id"));
INSERT INTO "por_car" ("year", "owner_id", "brand", "fuel_consumption", "kilometers", "rotation_speed", "image", "id", "car_model") SELECT "year", NULL, "brand", "fuel_consumption", "kilometers", "rotation_speed", "id", "car_model" FROM "por_car__old";
DROP TABLE "por_car__old";
CREATE INDEX "por_comments_4f331e2f" ON "por_comments" ("author_id");
CREATE INDEX "por_comments_cf8b1f8d" ON "por_comments" ("car_id");
CREATE INDEX "por_car_5e7b1936" ON "por_car" ("owner_id");
COMMIT;
